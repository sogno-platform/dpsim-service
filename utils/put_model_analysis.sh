
# This script hits three endpoints:
#
#  - /models      (PUT): to add one model
#  - /analysis    (PUT): to start analysing the model
#  - /analysis/id (GET): to get the status of the analysis
#
# This script expects the user to have checked out:
# git@git.rwth-aachen.de:acs/public/grid-data/cim-grid-data.git
# into their home directory.

set -o nounset
set -o errexit

if [ ! -d "/home/$USER/cim-grid-data" ];
then
    echo "Please clone git@git.rwth-aachen.de:acs/public/grid-data/cim-grid-data.git into /home/$USER"
    exit 1
fi

echo "Executing put command: 'curl -X POST "http://0.0.0.0:8081/models" -H  "accept: application/json" -H  "Content-Type: multipart/form-data" -F "files=@/home/$USER/cim-grid-data/WSCC-09/WSCC-09/WSCC-09_TP.xml\;type=text/xml" -F "files=@/home/$USER/cim-grid-data/WSCC-09/WSCC-09/WSCC-09_SV.xml\;type=text/xml" -F "files=@/home/$USER/cim-grid-data/WSCC-09/WSCC-09/WSCC-09_EQ.xml\;type=text/xml" -F "files=@/home/$USER/cim-grid-data/WSCC-09/WSCC-09/WSCC-09_DI.xml\;type=text/xml" -F "name=test" -F "profiles=EQ,TP,SV,DI" -F "version=cgmes_v2_4_15" )'"

PUT_MODEL=$(curl -o put_model_response.txt -w "%{http_code}" -X POST "http://0.0.0.0:8081/models" -H  "accept: application/json" -H  "Content-Type: multipart/form-data" -F "files=@/home/$USER/cim-grid-data/WSCC-09/WSCC-09/WSCC-09_TP.xml;type=text/xml" -F "files=@/home/$USER/cim-grid-data/WSCC-09/WSCC-09/WSCC-09_SV.xml;type=text/xml" -F "files=@/home/$USER/cim-grid-data/WSCC-09/WSCC-09/WSCC-09_EQ.xml;type=text/xml" -F "files=@/home/$USER/cim-grid-data/WSCC-09/WSCC-09/WSCC-09_DI.xml;type=text/xml" -F "name=test" -F "profiles=EQ,TP,SV,DI" -F "version=cgmes_v2_4_15" )

PUT_MODEL_RET_VALUE=$?
if [ $PUT_MODEL_RET_VALUE != 0 ];
then
    echo "PUT model failed with: $PUT_MODEL_RET_VALUE"
    exit 1
fi

if [ $PUT_MODEL != "200" ]; then
    echo PUT model command returned: $PUT_MODEL
    cat put_model_response.txt    
    exit 1
fi

MODEL_ID=$(cat put_model_response.txt | jq ".id")
echo Model id is: $MODEL_ID

PUT_ANALYSIS=$(curl -X POST "http://0.0.0.0:8082/analysis" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"modelid\":$MODEL_ID,\"name\":\"theAnalysis\",\"type\":\"PowerflowAnalysis\"}" )
ANALYSIS_ID=$(echo $PUT_ANALYSIS | jq ".analysis_id")
echo PUT analysis command returned: $PUT_ANALYSIS
echo Analysis id is: $ANALYSIS_ID

GET_STATUS=$(curl -X GET "http://0.0.0.0:8082/analysis/${ANALYSIS_ID}" -H  "accept: application/json")

echo "Status: $GET_STATUS"

GET_LOGS=$()

echo "TO GET LOGS: curl -X GET \"http://0.0.0.0:8082/analysis/${ANALYSIS_ID}/logs\" -H  \"accept: application/json\""
