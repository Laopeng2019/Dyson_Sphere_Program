import pandas as pd
import json

# This is a top-down approach of manufacture formula for both Chinese and English Dyson Sphere Program version
# 这是一个自上而下的设计方法，包含了中文和英文的戴森球计划的生产配方
class formula_calculation():
    def __init__(self,speed_zhizao = 0.75, speed_yelian = 1, speed_huagong = 1, speed_duizhuang = 1, 
    speed_caikuang = 1, speed_choushui = 1, speed_tanshe = 1, speed_fashe = 5,
    speed_cuiqu = 1.8, speed_jinglian = 1, speed_juzhen = 1, speed_keyan = 1,
    speed_caiji = 14.4, speed_jieshou = 1):

        self.formula=pd.read_excel('data.xlsx')
        self.formula.index = self.formula['生产物品']
        self.formula.drop(['生产物品'], axis=1, inplace=True)
        # with open('config.json') as f:
        #     self.speed_cn = json.load(f)
        self.speed_cn = {'制造':speed_zhizao, '冶炼':speed_yelian, '化工':speed_huagong, '粒子对撞':speed_duizhuang, 
        '采矿':speed_caikuang, '抽水':speed_choushui, '弹射':speed_tanshe, '发射':speed_fashe, '萃取':speed_cuiqu,
        '精炼':speed_jinglian, '矩阵':speed_juzhen, '科研':speed_keyan,'采集': speed_caiji, '接收': speed_jieshou,}

        self.exception = ['采矿','接收','采集','抽水']
        self.formula_result = {}
        self.init_flag = False
        self.load_config()


    def load_config(self):
        config = pd.read_excel('config.xlsx')
        # config.drop(['生产类型'], axis=1, inplace=True)
        self.speed_cn = config.to_dict()
        self.speed_cn

    # 计算输出框架
    def calculate(self, ingredient, quant_per_min):

        formula = self.calculate_recursive(ingredient, quant_per_min)
        
        temp2 = []
        for items in self.formula_result:
            temp = [items]
            for item in self.formula_result[items]:
                temp.append(self.formula_result[items][item])
            temp2.append(temp)
        columns = ['生产物品']
        for column in self.formula_result[ingredient].keys():
            columns.append(column)
        _result = pd.DataFrame(temp2,  columns=columns,)
        _result.to_excel('result.xlsx', index=False,)    
        return _result

    # 递归计算
    def calculate_recursive(self, ingredient, quant_per_min):
        formula = {}
        nomal_mineral_cover_quant = 5

        
        if ingredient not in self.formula.index:
            
            return {}
        else:
            if ingredient == '粒子宽带':
                ingredient
            sec_per_quant_predict = float(self.formula.loc[ingredient]['产出时间'] / self.formula.loc[ingredient]['产出数量']) 

            quant_per_sec = quant_per_min / 60
            sec_per_quant = 1 / quant_per_sec

            shengchanleixing = self.formula.loc[ingredient]['生产类型']

            quant_per_min_predict = (60/sec_per_quant_predict) * self.speed_cn[self.formula.loc[ingredient]['生产类型']]
            times = quant_per_min / quant_per_min_predict       
            times = round(times, 1)

            formula.setdefault(ingredient)
            formula[ingredient] = {'倍数':times, '类型':shengchanleixing, '预计速度(个每分钟)':quant_per_min_predict, 
            '需要速度(个每分钟)':quant_per_min, }
            # print('寻找配方:',ingredient,'需要速度(个每分钟)',quant_per_min,)
            
            # if self.init_flag == False:
            #     self.init_flag = True
            self.formula_scan(formula)
            transfer_speeds = []

            self.speed_scan([quant_per_min_predict], ingredient, shengchanleixing)


            contents = self.formula.loc[ingredient].to_list()
            
            for ind, content in enumerate(contents):
                columns = self.formula.columns[ind]
                if columns[:2]=='原料':
                    if pd.isna(content) is False:
                        next_times = contents[ind+1]
                        # 下一次计算所需的产量需要乘以配方所需原料数，同时除以当前配方的产量
                        next_quant_per_min = quant_per_min * next_times / self.formula.loc[ingredient]['产出数量']
                        next_formula = self.calculate_recursive(content, next_quant_per_min)
                        print(next_formula)
                        next_formula

        

        return formula

    def speed_scan(self, transfer_speeds, ingredient, shengchanleixing):
        # transfer_speeds = sorted(transfer_speeds, reverse=True)
        # 极限传送长度
        max_transfer_len, transfer_level = self.max_transfer_len_calculation(transfer_speeds, shengchanleixing)
        sorter_speeds = self.sorter_speed_calculation(transfer_speeds, shengchanleixing)

        # 本质上是叠加之前的信息，由于配方的原料输入速度都是一样的，所以没影响
        self.formula_result[ingredient].setdefault('最小分拣速度等级')
        self.formula_result[ingredient]['最小分拣速度等级'] = sorter_speeds
        self.formula_result[ingredient].setdefault('传送速度等级')
        self.formula_result[ingredient]['传送速度等级'] = transfer_level        
        self.formula_result[ingredient].setdefault('最适传送长度')
        self.formula_result[ingredient]['最适传送长度'] = max_transfer_len

    def formula_scan(self, formula):
        for item in formula:
            if item in self.formula_result:
                
                self.formula_result[item]['倍数'] = self.formula_result[item]['倍数'] + formula[item]['倍数']
                quant_per_min_predict = formula[item]['预计速度(个每分钟)']
                quant_per_min = formula[item]['需要速度(个每分钟)']
                # print('新增需求:',item,self.formula_result[item]['需要速度(个每分钟)'],'->',quant_per_min+self.formula_result[item]['需要速度(个每分钟)'],)
                self.formula_result[item]['预计速度(个每分钟)'] = quant_per_min_predict
                self.formula_result[item]['需要速度(个每分钟)'] = self.formula_result[item]['需要速度(个每分钟)'] + quant_per_min
                
            else:
                self.formula_result.setdefault(item)
                self.formula_result[item] = formula[item]  
        return 

    def max_transfer_len_calculation(self, transfer_speeds, shengchanleixing):
        ''' 传送速度等级和极限传送长度
        '''
        transfer_level = []
        max_transfer_len = []
        transfer_speed_temp = 0
        for ind, transfer_speed in enumerate(transfer_speeds):
            transfer_speed_temp = transfer_speed / 60

            if transfer_speed_temp <= 6:
                transfer_speed_temp = round(6 / transfer_speed_temp , 1)
                max_transfer_len.append(str(transfer_speed_temp)) 
                transfer_level.append('1') 
            elif transfer_speed_temp <= 12 :
                max_transfer_len.append(str(round(6/transfer_speed_temp, 1))) 
                transfer_level.append('2') 
            elif transfer_speed_temp <= 30 :
                max_transfer_len.append(str(round(30/transfer_speed_temp, 1))) 
                transfer_level.append('3') 
            else: 
                max_transfer_len.append(str(round(30/transfer_speed_temp, 1))) 
                transfer_level.append('>3') 
            if shengchanleixing in self.exception:
                transfer_speeds[ind] = '无'
                max_transfer_len[ind] = '无'
                continue 


        return ','.join(max_transfer_len), ','.join(transfer_level)

    def sorter_speed_calculation(self, transfer_speeds, shengchanleixing):
        '''最小分拣速度计算
        '''
        for ind, transfer_speed in enumerate(transfer_speeds):
            if shengchanleixing in self.exception:
                transfer_speeds[ind] = '无'
                continue            
            if transfer_speed / 60  <= 1.5:
                transfer_speeds[ind] = '1'
            elif transfer_speed / 60  <= 3:
                transfer_speeds[ind] = '2'
            elif transfer_speed / 60  <= 36:
                transfer_speeds[ind] = '3'
            else:
                transfer_speeds[ind] = '3'


        return ','.join(transfer_speeds)


use = formula_calculation()
# 产物输入
formula = use.calculate('白糖', 1200)



