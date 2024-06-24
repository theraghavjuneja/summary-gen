file_path = "response.txt"
output_file_path = "response_with_empty_lines.txt"

with open(file_path, "r") as f_in, open(output_file_path, "w") as f_out:
    for line in f_in:
        f_out.write(line.strip() + "\n") 
        f_out.write("\n")  
