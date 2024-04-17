from TextSummarizer.pipeline.data_ingestion import DataIngestionTrainingPipeline
from TextSummarizer.pipeline.data_validation import DataValidationTrainingPipeline
from TextSummarizer.pipeline.data_transformation import DataTransformationTrainingPipeline
from TextSummarizer.pipeline.model_trainer import ModelTrainerTrainingPipeline
from TextSummarizer.pipeline.model_evaluation import ModelEvaluationTrainingPipeline
from TextSummarizer.logging import logger

PIPELINES = []

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>> Stage: {STAGE_NAME} Started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> Stage: {STAGE_NAME} Completed <<<<<")
except Exception as ex:
    logger.exception(ex)
    raise ex

logger.info("=================================================")

STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>> Stage: {STAGE_NAME} Started <<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>> Stage: {STAGE_NAME} Completed <<<<<")
except Exception as ex:
    logger.exception(ex)
    raise ex

logger.info("=================================================")

STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>>> Stage: {STAGE_NAME} Started <<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>> Stage: {STAGE_NAME} Completed <<<<<")
except Exception as ex:
    logger.exception(ex)
    raise ex

logger.info("=================================================")

STAGE_NAME = "Model Trainer Stage"

try:
    logger.info(f">>>>> Stage: {STAGE_NAME} Started <<<<<")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>> Stage: {STAGE_NAME} Completed <<<<<")
except Exception as ex:
    logger.exception(ex)
    raise ex

logger.info("=================================================")

STAGE_NAME = "Model Evaluation Stage"

try:
    logger.info(f">>>>> Stage: {STAGE_NAME} Started <<<<<")
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logger.info(f">>>>> Stage: {STAGE_NAME} Completed <<<<<")
except Exception as ex:
    logger.exception(ex)
    raise ex