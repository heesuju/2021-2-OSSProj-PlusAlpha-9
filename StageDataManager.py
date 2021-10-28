import json
from Stage import Stage
from collections import OrderedDict
class StageDataManager:

    @staticmethod
    def loadStageData():
        with open('stagedata.json') as f:
            stageData = json.load(f,object_pairs_hook=OrderedDict)
        return stageData

    
    @staticmethod
    def unlockNextStage(stage):
        with open('stagedata.json', 'r') as f:
            json_data = json.load(f,object_pairs_hook=OrderedDict)

        try:
            json_data["chapter"][stage.chapter][str(list(json_data["chapter"][stage.chapter].keys()).index(f"{stage.stage}")+2)][6] = 1
        except:
            pass
            
        with open('stagedata.json', 'w', encoding='utf-8') as make_file:
            json.dump(json_data, make_file, indent="\t")