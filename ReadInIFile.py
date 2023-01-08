import os
import configparser
import re
import abc
class InIFileReader:
    _DataList = []#_private 属性
    def __init__(self,InIFileName):
        self._ConfObj =  configparser.ConfigParser()
        self._ConfObj.read(InIFileName,encoding='gbk')
    def ReadWFTName(self):
        return self._ConfObj.get(section='CreateSettings',option="WFTName")
    def ReadSignals(self):
        return self._ConfObj.get(section='CreateSettings',option="Signal")
    def ReadAllOrinalData(self):
        self._DataList.clear()
        for key_in_SectionRegList in self._ConfObj.options('RegList'):
            value_in_SectionRegListOption = self._ConfObj.get("RegList",key_in_SectionRegList)
            self._DataList.append(value_in_SectionRegListOption)
        # print(f"ReadAllOrinalData {self._DataList}")
        return self._DataList
    @abc.abstractmethod
    def _DataFomatCheck(self,InputStr):#抽象方法 其他通信协议的派生类需要各自实现 _protect方法
        pass
class I2C(InIFileReader):#继承InIFileReader的一些方法
    def __init__(self,InIFileName):
        InIFileReader.__init__(self, InIFileName)
        self.__DataList = []
    def ReadSlaveID(self):
        return self._ConfObj.get(section='CreateSettings',option="SlaveID")
    def ReadDataAfterCheck(self):
        for SigleSequence in self.ReadAllOrinalData():
            if self._DataFomatCheck(SigleSequence):
                self.__DataList.append(SigleSequence)
            else:
                print(f"{SigleSequence} Data has been abundant!!!")
        return self.__DataList
    def _DataFomatCheck(self, InputStr):
        #I2C check the data form ini file format
        ReObj = re.match(r'([c-d]?),0x([a-f0-9]?[a-f0-9]?[a-f0-9]?[a-f0-9]?),0x([a-f0-9]?[a-f0-9]?),'
                         , InputStr, re.I)  # 数据的正则表达式
        if ReObj is not None:
            # print(ReObj)
            # print(ReObj.groups())
            return True
        else:
            print(f"{InputStr} Data Formmat error!!!")
            return False
# def DataFomatCheck(InputStr):
#     #check the data form ini file format
#     ReObj = re.match(r'([c-d]?),0x([a-f0-9]?[a-f0-9]?[a-f0-9]?[a-f0-9]?),0x([a-f0-9]?[a-f0-9]?),'
#                      , InputStr, re.I)  # 数据的正则表达式
#     if ReObj is not None:
#         # print(ReObj)
#         # print(ReObj.groups())
#         return True
#     else:
#         print(f"{InputStr} Data Formmat error!!!")
#         return False
# conf = configparser.ConfigParser()
# conf.read('test.ini',encoding='gbk')
# ALL_sections = conf.sections()#返回一个list 包含所有的sections
# print(ALL_sections)
# for SigleSection in ALL_sections:
#     option = conf.options(SigleSection)#获取该section中 所有的key为string list
#     # print(option)
#     items = conf.items(SigleSection)#获取该section中 所有的键值对 为 元组 list
#     # print(items)
#     for key_in_option in option:
#         value_in_option = conf.get(SigleSection,key_in_option)#获取section 中，key值对应的value
#         if SigleSection=="RegList":
#             if IniDataFomatCheck(value_in_option):
#                 print(f"value is {value_in_option}")
#         else:
#             print(value_in_option)
# I2CReadTest  = I2C('test.ini')
# print(I2CReadTest.ReadSignals())
# print(I2CReadTest.ReadWFTName())
# print(I2CReadTest.ReadSlaveID().upper())
# # print(I2CReadTest.ReadAllOrinalData())
# for seqence in I2CReadTest.ReadAllOrinalData():
#     print(seqence)
# print('\n')
# # for seqenceaftercheck in I2CReadTest.ReadDataAfterCheck():
# #     print(seqenceaftercheck)
# print(I2CReadTest.ReadDataAfterCheck())
