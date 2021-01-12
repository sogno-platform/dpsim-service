# DPsim Service

This is a server which provides an [OpenAPI](http://spec.openapis.org/oas/v3.0.3) REST API for [DPSim](https://git.rwth-aachen.de/acs/public/simulation/dpsim/dpsim), a solver library for dynamic power system simulation. The DPsim service pulls CIM grid data from the [CIM service](https://github.com/cim-iec/cim-service).

The server is based on [connexion](https://github.com/zalando/connexion) which itself builds upon [flask](https://flask.palletsprojects.com/en/1.1.x/).
The API is specified in the [openapi.yaml](openapi.yaml).

## Requirements

- Python 3.5.2+
- DPSim Version xy
- CIMpy python packages and dependencies specified by [requirements-cimpy.txt](./requirements-cimpy.txt). Install them with `pip3 install -r requirements-cimpy.txt`

## Usage

To run the server, please execute the following from the root directory:

```bash
python3 server.py
```

For manual interaction and a rendered specification open http://localhost:8080/ui/ in your Browser.

## Development:

Notes for developers:

- The repository contains set of vscode configurations at (.vscode)[.vscode/]

### Code Structure

The [server.py](./server.py) invokes the connexion server with the _openapi.yaml_ as argument. The connexion server then parses the yaml and provides the general server functionality.
The developer then has to provide the callbacks to the service which should be called by the API.
The name of the callback function is specified in the _openapi.yaml_ as `operationID` (example: `operationId: cimadapter.get_models`).
The basic job is then to provide these callbacks.

The convention for the ANM4L server is to put the callbacks into the project root with a name like `XYZadapter.py`.

The _openapi-generator_ also generates a set of classes which correspond to the `schema` from the openapi.yaml.
These can be used to ease the parsing of requests and the generation of responses.
All of these classes are located at [models](./models/).

### Code Generation/API Changes

The fundamental code structure is generated with the [OpenAPITool openapi-generator]( https://github.com/OpenAPITools/openapi-generator).
If the openapi.yaml has changed, you can run the [generate_api_code.sh](generate_api_code.sh) script to generate these files again.

**However, these files must be adapted manually!** The quality of the generated code is not sufficient.
Examples of what must be adapted:

- _openapi-generator_ puts all the server files into a folder `openapi`, which is this an unnecessary hierarchy.
You need to copy the generated files to the corresponding folder in the repository **and** fix the `import` lines in the python code.
- _openapi-generator_ generates some useless files. Not all "models" are needed for the implementation
- _openapi-generator_ creates sometimes unnecessary imports. Characteristic examples: `connexion`, `six`, `json`. Also sometimes files are imported twice.

**Recommended approach:**

Generate the files and then use a diff editor such as [meld](https://meldmerge.org) to selectively import the changed code. Example:

```bash
meld generated/openapi_server/models models
```

### Testing

This project uses `pytest` for integration tests. All integration test can be found in [test](test/). To invoke it manually call:

```bash
pytest  -cov test/
```

(pytest should easily integrate into your IDE...)
