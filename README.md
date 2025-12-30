
# smartdoc

A CLI for analyzing OpenAPI Specification (OAS) files. smartdoc scores OAS files against several metrics:

* Description coverage
* Description quality 
* Naming consistency
* Example adequacy


## Prerequisites

To install this project, you need:

* pip 
* Python 3.10 or later
* An OpenAI [API Key](https://platform.openai.com)
  
## Run locally

1. Clone the project:

```bash
  git clone https://github.com/itsdeannat/smartdoc
```

2. Go to the project directory:

```bash
  cd smartdoc
```

3. Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

4. Install project dependencies:

```bash
pip install -r requirements.txt
```

5. Create a `.env` file in the root directory and add your API key:

```bash
OPENAI_API_KEY=your_key_here
```

6. Run the CLI:

```bash
smartdoc check [oas_file]
```




## Usage/Examples

```bash
smartdoc check openapi.yaml
```

```bash
File './openai.yaml' found.
OAS file loaded.
API key loaded: True
Checking the OAS file for issues...
```


High-level findings:

```bash
- Many descriptions are missing or empty: 14 of the 22 descriptionable locations are missing or blank.
- There is a single request example (POST /orders.sampleOrder). There are no response examples.
- Naming is broadly consistent: snake-free camelCase for field names (productId, orderId, quantity) and PascalCase for schema names (NewOrder, OrderItem).
- Several schema properties and operation parameters lack meaningful descriptions; some operation response descriptions are also empty.
- Basic validation is present (quantity minimum), but status values are not constrained or documented.
```

Metric scores:
```bash
Metric scores (0–100)
1) Description coverage: 36% (8/22 descriptions present)
2) Description clarity: 60% — descriptions that exist are mostly functional but many are terse or non-informative (e.g., "The ID"). A few are reasonable (e.g., "Deletes the order."), but overall clarity is low.
3) Naming consistency: 90% — consistent use of camelCase for fields and PascalCase for schema names; paths and operations are sensibly named.
4) Example adequacy: 25% — a single request example exists (good for the POST body), but there are no response examples and no examples for other operations or error cases.
```

Suggested improvements:

```bash
Concise prioritized checklist to improve the spec quickly
- Fill missing descriptions for operations, parameters, responses, and schema properties (highest priority).
- Add response examples for success and error cases.
- Add a reusable Error schema and reference it for 4xx responses.
- Add operationId and tags to the operations.
- Document status field values (enum or descriptive list).
- Add Location header description for 201 if applicable.
```

## CLI help

For more information about `smartdoc`, use `--help`:

```bash
$ smartdoc --help
```

**Note**: `check` is the only available command. More commands will be added later.
## Authors

[@itsdeannat](https://www.github.com/itsdeannat)

