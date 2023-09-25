#!/bin/bash -x

pushd /home/vint/workspace/ace
./clean.sh
python3 /home/vint/workspace2/ScriptGUI/difficult/do_difficult.py /home/vint/workspace/ace/ ace/
./ace-do-all-xls.sh
python3 /home/vint/workspace2/ScriptGUI/difficult/checker.py /home/vint/workspace/ace/
echo "completed"
popd
