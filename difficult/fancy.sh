#!/bin/bash -x

pushd /home/vint/workspace/fancymoda/
./clean.sh
python3 /home/vint/workspace2/ScriptGUI/difficult/do_difficult.py /home/vint/workspace/fancymoda/ fancymoda/
./fancy-do-all-xls.sh
python3 /home/vint/workspace2/ScriptGUI/difficult/checker.py /home/vint/workspace/fancymoda/
echo "completed"
popd
