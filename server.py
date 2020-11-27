from flask import Flask, Response, stream_with_context
from flask_cors import CORS

import pandas as pd

import definitions

# Flask web server definition
webserver = Flask(__name__)
CORS(webserver)


# Constants
data_file_path = "./data.csv.bz2"

@webserver.route('/stream', methods=['GET'])
def stream():

    # Load csv into dataframe
    dataframe = pd.read_csv(data_file_path, header=None)

    def generate():
        for row in dataframe.values:
            yield str(row).strip('[]').replace(" ", ",").replace("\n", "") + '\n'


    return Response(stream_with_context(generate()), mimetype='text/csv')

if __name__ == '__main__':
    webserver.run(host="localhost", port=definitions.port, debug=True)
