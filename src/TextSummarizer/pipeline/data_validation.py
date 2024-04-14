from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.components.data_validation import DataValidation

class DataValidationTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.validate_all_files_exists()
        except Exception as ex:
            raise ex