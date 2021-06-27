# umlToAPI
Berikut ini adalah deskripsi singkat, bagaimana merubah data staruml, ke openapi sesuai prosedur berikut ini.
kemudian, merubah file openapi3 menjadi swagger2

how to run
1. make venv
    python -m venv <folder>
2. run python
    python test.py
3. how to convert
    api-spec-converter --from=openapi_3 --to=swagger_2 --syntax=yaml Class_Dashboard.yml > swagger.yaml
4. change variable test.py
    fileYaml = 'swagger.yaml'

more info
https://github.com/LucyBot-Inc/api-spec-converter.git
https://edi3.org/specs/edi3-uml-profile/develop/
