from transformers import AutoTokenizer, pipeline
from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.entity import ModelEvaluationConfig

class PredictionPipeline:
    def __init__(self) -> None:
        self.config: ModelEvaluationConfig = ConfigurationManager().get_model_evaluation_config()
    
    def predict(self, text):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs = {
            "length_penalty": 0.8,
            "num_beams": 8,
            "max_length": 128
        }
        
        pipe_line = pipeline(
            task="summarization",
            model=self.config.model_path,
            tokenizer=tokenizer
        )
        
        print("Dialogue: ")
        print(text)
        
        output = pipe_line(text, **gen_kwargs)[0]["summary_text"]
        print("\nModel Summary: ")
        print(output)
        
        return output