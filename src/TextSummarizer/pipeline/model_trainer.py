from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.entity import ModelTrainerConfig

class ModelTrainerTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTrainerConfig(config=model_trainer_config)
            model_trainer.train()
        except Exception as ex:
            raise ex