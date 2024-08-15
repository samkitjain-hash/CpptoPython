import streamlit as st

def cpp_to_py_format(cpp_code):
    lines = cpp_code.split('\n')
    processed_lines = []
    braces = []
    max_line_length = 0

    for line in lines:
        stripped_line = line.rstrip()

        if '{' in stripped_line or '}' in stripped_line:

            line_without_brace = stripped_line.replace('{', '').replace('}', '')

            processed_lines.append(line_without_brace.rstrip())
            max_line_length = max(max_line_length, len(line_without_brace))
            
            # Store the brace with its corresponding line
            #TODO here append '{' if found '{' else '}'
            if '{' in stripped_line:
                braces.append('{')
            else:
                braces.append('}')
        else:
            # If no brace, just add the line as is
            processed_lines.append(line.rstrip())
            max_line_length = max(max_line_length, len(line.rstrip()))
            braces.append('')
    
    # Combine lines and braces
    final_lines = []
    for i in range(len(processed_lines)):
        if braces[i]:
            final_lines.append(processed_lines[i] + ' ' * (max_line_length - len(processed_lines[i])) + braces[i])
        else:
            final_lines.append(processed_lines[i])
    
    return '\n'.join(final_lines)

# Example usage
cpp_code = """
int main(){
    if(a==2){
        cout<<"yes"<<endl;
    }else{
        cout<<"NO"<<endl;
    }
}
"""
def main():
    st.title("C++ to Python Formatter")

    cpp_code = st.text_area("Enter C++ Code:", height=300)

    if st.button("Format Code"):
        if cpp_code:
            formatted_code = cpp_to_py_format(cpp_code)
            st.subheader("Formatted Code:")
            st.code(formatted_code, language='python')
        else:
            st.warning("Please enter some C++ code to format.")

if __name__ == "__main__":
    main()
