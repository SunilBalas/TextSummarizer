import os
from TextSummarizer.logging import logger
from TextSummarizer.entity import (DataValidationConfig)

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
    
    def validate_all_files_exists(self) -> bool:
        try:
            validation_status = None
            
            all_files = os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset"))
            
            if os.path.exists(self.config.STATUS_FILE):
                os.remove(self.config.STATUS_FILE)
            
            for file in all_files:
                validation_status = False if file not in self.config.ALL_REQUIRED_FILES else True
                
                with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation Status: {validation_status}")
            
            return validation_status
        except Exception as ex:
            raise ex