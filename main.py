from TextSummarizer.pipeline.data_ingestion import DataIngestionTrainingPipeline
from TextSummarizer.pipeline.data_validation import DataValidationTrainingPipeline
from TextSummarizer.pipeline.data_transformation import DataTransformationTrainingPipeline
from TextSummarizer.pipeline.model_trainer import ModelTrainerTrainingPipeline
from TextSummarizer.pipeline.model_evaluation import ModelEvaluationTrainingPipeline
from TextSummarizer.logging import logger

STAGES = [
    ["Data Ingestion", DataIngestionTrainingPipeline],
    ["Data Validation", DataValidationTrainingPipeline],
    ["Data Transformation", DataTransformationTrainingPipeline],
    ["Model Trainer", ModelTrainerTrainingPipeline],
    ["Model Evaluation", ModelEvaluationTrainingPipeline]
]

for stage in STAGES:
    name, pipeline = stage

    try:
        logger.info(f">>>>> Stage: {name} Started <<<<<")
        data_pipeline = pipeline()
        data_pipeline.main()
        logger.info(f">>>>> Stage: {name} Completed <<<<<")
    except Exception as ex:
        logger.exception(ex)
        raise ex

    logger.info("=================================================")