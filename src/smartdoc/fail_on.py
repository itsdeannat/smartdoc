import sys
import typer

def evaluate_fail_on_condition(analysis_result, fail_on: str):
    """
    Evaluates a fail-on condition for full analysis and exits if threshold is exceeded.

    - analysis_result: FullAnalysisSchema object
    - fail_on: string in the form CATEGORY.METRIC=THRESHOLD
    """
    if "=" not in fail_on:
        raise typer.BadParameter(
            "--fail-on must be in the format CATEGORY.METRIC=THRESHOLD"
        )

    key, threshold_str = fail_on.split("=")
    try:
        threshold = int(threshold_str)
    except ValueError:
        raise typer.BadParameter(f"Threshold must be an integer: {threshold_str}")

    if "." not in key:
        raise typer.BadParameter(
            "Full analysis requires --fail-on in CATEGORY.METRIC=THRESHOLD format"
        )

    category, metric_name = key.split(".", 1)
    category_obj = getattr(analysis_result, category, None)

    metric_value = getattr(category_obj, metric_name, None)
    if metric_value is None:
        print(f"Metric '{key}' not found in analysis result")
        sys.exit(1)
    elif metric_value > threshold:
        print("Fail-on triggered, exiting 1")
        sys.exit(1)
