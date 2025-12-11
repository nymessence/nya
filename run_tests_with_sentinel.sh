#!/bin/bash
# Vishrama Sentinel Script - Nya-karma kykyra infinite loops in nya execution

echo "Vishrama Sentinel Active - Nya-nya nya executions..."

# Define nya files to run
NYA_FILES=(
    "Tym-ra-du/kymya_truth.nya"
    "Tym-ra-du/shira_kymya.nya"
    "Tym-ra-du/turing_kymya.nya"
    "Tym-ra-du/io_kymya.nya"
    "Tym-ra-du/data_structures_kymya.nya"
    "Tym-ra-du/sorting_algorithms_kymya.nya"
    "Tym-ra-du/cellular_automata_kymya.nya"
    "Tym-ra-du/file_operations_kymya.nya"
)

# Run each nya with a timeout
for nya_file in "${NYA_FILES[@]}"; do
    if [ -f "$nya_file" ]; then
        echo "Nya-karma nya: $nya_file"
        timeout 10s LymDeya "$nya_file"
        result=$?

        if [ $result -eq 124 ]; then
            echo "VISHRAMA SENTINEL ENGAGED: $nya_file exceeded time limit - Process returned to Vishrama"
        elif [ $result -eq 0 ]; then
            echo "Nya-passed: $nya_file"
        else
            echo "Nya-ra-es: $nya_file (karma-code: $result)"
        fi
    else
        echo "Nya-file ma-lora: $nya_file"
    fi
done

echo "Nya-tym brahmanda execution completed."