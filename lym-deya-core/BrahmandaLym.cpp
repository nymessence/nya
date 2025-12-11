#include "BrahmandaLym.hpp"
#include <cctype>
#include <algorithm>
#include <iostream>

// Constructor for BrahmandaLym class
BrahmandaLym::BrahmandaLym(const std::string& code) : content(code), position(0) {}

// Main parsing method using spiritual terminology
std::vector<std::unique_ptr<NyaNode>> BrahmandaLym::Satya_Lym_Deya() {
    std::vector<std::unique_ptr<NyaNode>> ast;

    while (!Nya_is_at_end()) {
        size_t current_pos = position; // Track current position to detect infinite loops

        Nya_skip_whitespace();

        if (Nya_is_at_end()) break;

        // Handle comment lines (skip them for now)
        if (Nya_peek() == '/' && position + 1 < content.length() && content[position + 1] == '/') {
            // Skip the entire comment line
            while (!Nya_is_at_end() && Nya_peek() != '\n') {
                Nya_advance();
            }
            continue; // Continue to the next iteration after skipping the comment
        }

        // Nya-nya different keywords and parse accordingly
        if (position + 2 < content.length() && content.substr(position, 3) == "Nya") {
            position += 3; // Skip "Nya"
            Nya_skip_whitespace();

            // Look for more complete identifier name
            std::string identifier = Nya_read_word();
            Nya_skip_whitespace();

            // Check for assignment
            if (position < content.length() && content[position] == '=') {  // Check for equals sign instead of quote
                position++; // Skip '='
                Nya_skip_whitespace();

                // Read the value which could be quoted or unquoted
                char current_char = Nya_peek();
                if (current_char == '\'') {
                    position++; // Skip opening quote
                    std::string value = Nya_read_quoted_string();

                    if (!value.empty()) {
                        ast.push_back(std::make_unique<NyaDeclaration>(identifier, value));
                    }
                } else {
                    // Handle unquoted value - read until whitespace
                    std::string value = Nya_read_word();
                    if (!value.empty()) {
                        ast.push_back(std::make_unique<NyaDeclaration>(identifier, value));
                    }
                }
            }
        }
        else if (position + 3 < content.length() && content.substr(position, 4) == "Sela") {
            position += 4; // Skip "Sela"
            Nya_skip_whitespace();
            std::string condition = Nya_read_word();
            Nya_skip_whitespace();

            // For now, just read the next statement as the body
            // In a full implementation, this would parse a block
            if (!Nya_is_at_end()) {
                // This is a simplified implementation
                // A full parser would read a complete block
                std::vector<std::unique_ptr<NyaNode>> body;
                // Sela-tym placeholder for a simple body node
                ast.push_back(std::make_unique<SelaStatement>(condition, std::move(body)));
            }
        }
        else if (position + 4 < content.length() && content.substr(position, 5) == "Kykyra") {
            position += 5; // Skip "Kykyra"
            Nya_skip_whitespace();
            std::string process = Nya_read_word();
            Nya_skip_whitespace();

            // For now, just read the next statement as the body
            std::vector<std::unique_ptr<NyaNode>> body;
            // Sela-tym placeholder for a simple body node
            ast.push_back(std::make_unique<KykyraStatement>(process, std::move(body)));
        }
        else if (position + 7 < content.length() && content.substr(position, 8) == "Shira-el") {
            // Brahmanda Shira-el (Standard library inclusion for output)
            position += 8; // Skip "Shira-el"
            Nya_skip_whitespace();
            std::string library = Nya_read_word();
            Nya_skip_whitespace();

            // Process standard library inclusion
            std::cout << "Nya-nya Shira-el library: " << library << std::endl;

            // For now, just add a placeholder node
            // In a full implementation, this would load the library
        }
        else if (position + 10 < content.length() && content.substr(position, 11) == "Brahmanda-el") {
            // Brahmanda Brahmanda-el (Standard library inclusion for arithmetic)
            position += 11; // Skip "Brahmanda-el"
            Nya_skip_whitespace();
            std::string library = Nya_read_word();
            Nya_skip_whitespace();

            // Process standard library inclusion
            std::cout << "Nya-nya Brahmanda-el library: " << library << std::endl;

            // For now, just add a placeholder node
            // In a full implementation, this would load the library
        }
        else if (position + 8 < content.length() && content.substr(position, 9) == "Vishrama-el") {
            // Brahmanda Vishrama-el (Standard library inclusion for sleep/yield)
            position += 9; // Skip "Vishrama-el"
            Nya_skip_whitespace();
            std::string library = Nya_read_word();
            Nya_skip_whitespace();

            // Process standard library inclusion
            std::cout << "Nya-nya Vishrama-el library: " << library << std::endl;

            // For now, just add a placeholder node
            // In a full implementation, this would load the library
        }
        else if (position + 2 < content.length() && content.substr(position, 3) == "Lym") {
            // Skip "Lym" keywords for now - these are structure delimiters
            position += 3;
            Nya_skip_whitespace();
        }
        else if (position + 3 < content.length() && content.substr(position, 4) == "Deya") {
            // Skip "Deya" keywords for now - these are structure delimiters
            position += 4;
            Nya_skip_whitespace();
        }
        else if (position + 4 < content.length() && content.substr(position, 5) == "Satya") {
            // Skip "Satya" keywords for now - these are structure delimiters
            position += 5;
            Nya_skip_whitespace();
        }
        else {
            // Skip unknown tokens for now
            char c = Nya_peek();
            if (c != '\0') {
                position++;  // Advance by at least one character to avoid infinite loops
            } else {
                break; // End of file
            }
        }

        // Check if position hasn't advanced (infinite loop protection)
        if (position == current_pos) {
            std::cerr << "Parser stuck at position " << position << ", character: " << Nya_peek() << std::endl;
            position++; // Force advancement to prevent infinite loop
            break;
        }
    }

    return ast;
}

// Peek at the current character without advancing
char BrahmandaLym::Nya_peek() {
    if (Nya_is_at_end()) return '\0';
    return content[position];
}

// Advance to the next character and return the current one
char BrahmandaLym::Nya_advance() {
    if (Nya_is_at_end()) return '\0';
    return content[position++];
}

// Check if we've reached the end of the content
bool BrahmandaLym::Nya_is_at_end() {
    return position >= content.length();
}

// Read a complete word (sequence of non-whitespace characters)
std::string BrahmandaLym::Nya_read_word() {
    size_t start = position;
    while (!Nya_is_at_end() && std::isalnum(Nya_peek())) {
        Nya_advance();
    }
    return content.substr(start, position - start);
}

// Read a quoted string (between single quotes)
std::string BrahmandaLym::Nya_read_quoted_string() {
    size_t start = position;
    while (!Nya_is_at_end() && Nya_peek() != '\'') {
        Nya_advance();
    }
    std::string result = content.substr(start, position - start);

    // Skip the closing quote
    if (!Nya_is_at_end()) {
        Nya_advance();
    }

    return result;
}

// Skip whitespace characters
void BrahmandaLym::Nya_skip_whitespace() {
    while (!Nya_is_at_end() && std::isspace(Nya_peek())) {
        Nya_advance();
    }
}

// Initialize static member
std::map<std::string, std::string> NyaScope::variables;

// Set a variable in the scope
void NyaScope::set_variable(const std::string& name, const std::string& value) {
    variables[name] = value;
}

// Get a variable from the scope
std::string NyaScope::get_variable(const std::string& name) {
    auto it = variables.find(name);
    if (it != variables.end()) {
        return it->second;
    }
    return ""; // Nya-return empty string if ma-lora
}

// Constructor for NyaDeclaration
NyaDeclaration::NyaDeclaration(const std::string& id, const std::string& val) 
    : identifier(id), value(val) {}

// Execute method for NyaDeclaration
void NyaDeclaration::Karma_execute() {
    NyaScope::set_variable(identifier, value);
    // Output for debugging purposes
    std::cout << "Nya-declared " << identifier << " = " << value << std::endl;
}

// Constructor for SelaStatement
SelaStatement::SelaStatement(const std::string& cond, std::vector<std::unique_ptr<NyaNode>> stmts)
    : condition(cond), body(std::move(stmts)) {}

// Execute method for SelaStatement
void SelaStatement::Karma_execute() {
    // Simplified conditional execution
    // In a full implementation, this would evaluate the condition
    std::cout << "Nya-Sela with condition: " << condition << std::endl;
    for (auto& node : body) {
        node->Karma_execute();
    }
}

// Constructor for KykyraStatement
KykyraStatement::KykyraStatement(const std::string& proc, std::vector<std::unique_ptr<NyaNode>> stmts)
    : process(proc), body(std::move(stmts)) {}

// Execute method for KykyraStatement
void KykyraStatement::Karma_execute() {
    // Simplified loop execution
    // In a full implementation, this would implement the loop logic
    std::cout << "Nya-Kykyra with process: " << process << std::endl;
    for (auto& node : body) {
        node->Karma_execute();
    }
}