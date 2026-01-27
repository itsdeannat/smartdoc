import sys
import typer

def evaluate_fail_on_condition(analysis_result, fail_on: list[str]):
    """
    Evaluates a fail-on condition for full analysis and exits if threshold is exceeded.

    - analysis_result: FullAnalysisSchema object
    - fail_on: string in the form CATEGORY.METRIC=THRESHOLD
    # """
            
    for condition in fail_on:
        
        results = []
        
        print(f"Evaluating {condition}...")
        key, threshold_str = condition.split("=")
        try:
            threshold = int(threshold_str)
        except ValueError:
            raise typer.BadParameter(f"Threshold must be an integer: {threshold_str}")

        if "." not in key:
            raise typer.BadParameter(
                "--fail-on must be in the format CATEGORY.METRIC=THRESHOLD"
            )

        category, metric_name = key.split(".", 1)
        category_obj = getattr(analysis_result, category, None)

        metric_value = getattr(category_obj, metric_name, None)
        if metric_value is None:
            print(f"Metric '{key}' not found in analysis result")
            sys.exit(1)
        elif metric_value <= threshold:
            result.append(True)
            print("Threshold not met.")
            continue
        elif metric_value > threshold:
            results.append(False)
            print(f"Threshold exceeded: value={metric_value}, threshold={threshold}.")
            continue
            
        for result in results:
            if result is False:
                raise typer.Exit(code=1)
            
            
        
