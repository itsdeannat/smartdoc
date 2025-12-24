import analysis_engine.prompter as prompter
import oas.file_handler as file_handler


def main():
    oas_path = "sample_oas.yml"
    content = file_handler.load_file(oas_path)
    prompter.analyze_content(content)
    
    
if __name__ == "__main__":
    main()