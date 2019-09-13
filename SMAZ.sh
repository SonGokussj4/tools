#!/usr/bin/bash

echo "before 1st question"
read -rp "Question [Y/n]? " hmm
case "${hmm:0:1}" in
    y|Y )
        echo yes
    ;;
    * )
        echo No
        exit
    ;;
esac
sleep 1
echo "before 2nd question"
sleep 1

# read -rp "Question2 [Y/n]? " answer2
# case "${answer2:0:1}" in
#     y|Y )
#         echo yes
#     ;;
#     * )
#         echo No
#         exit
#     ;;
# esac
echo "before exit"
sleep 1
echo "End of script"

# echo $(pwd)
# echo "\$0: $0"
# echo "\$#: $#"
# echo "\$1: $1"
# echo "\$2: $2"

# for i in "$@"; do
#     echo "echo $i;"
# done

# res=$*
# echo "$res"
# eval "$res"
