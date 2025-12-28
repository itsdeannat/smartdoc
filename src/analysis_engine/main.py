import analysis_engine.llm_client as llm_client
import oas.yaml_loader as yaml_loader


def main():
    oas_path = "sample_oas.yml"
    content = yaml_loader.load_file(oas_path)
    llm_client.analyze_spec(content)
    
    
if __name__ == "__main__":
    main()