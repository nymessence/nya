#ifndef BRAHMANDALYM_HPP
#define BRAHMANDALYM_HPP

#include <string>
#include <vector>
#include <memory>
#include <map>

// BrahmandaLym: Nymya AST class for the Nya language
class BrahmandaLym {
private:
    std::string content;
    size_t position;

public:
    BrahmandaLym(const std::string& code);
    std::vector<std::unique_ptr<class NyaNode>> Satya_Lym_Deya();  // Parse method with spiritual terminology

private:
    char Nya_peek();  // Peek at current character
    char Nya_advance();  // Advance to next character
    bool Nya_is_at_end();  // Check if at end of file
    std::string Nya_read_word();  // Read a complete word
    std::string Nya_read_quoted_string();  // Read a quoted string
    void Nya_skip_whitespace();  // Skip whitespace characters
};

// Base class for all AST nodes
class NyaNode {
public:
    virtual ~NyaNode() = default;
    virtual void Karma_execute() = 0;  // Execute with spiritual terminology
};

// Class representing a Nya declaration (Nya identifier = value)
class NyaDeclaration : public NyaNode {
private:
    std::string identifier;
    std::string value;

public:
    NyaDeclaration(const std::string& id, const std::string& val);
    void Karma_execute() override;
};

// Class representing a Sela (conditional) statement
class SelaStatement : public NyaNode {
private:
    std::string condition;
    std::vector<std::unique_ptr<NyaNode>> body;

public:
    SelaStatement(const std::string& cond, std::vector<std::unique_ptr<NyaNode>> stmts);
    void Karma_execute() override;
};

// Class representing a Kykyra (loop) statement
class KykyraStatement : public NyaNode {
private:
    std::string process;
    std::vector<std::unique_ptr<NyaNode>> body;

public:
    KykyraStatement(const std::string& proc, std::vector<std::unique_ptr<NyaNode>> stmts);
    void Karma_execute() override;
};

// NyaScope: Class to manage variable scope
class NyaScope {
private:
    // Map to store variables and their values
    static std::map<std::string, std::string> variables;

public:
    static void set_variable(const std::string& name, const std::string& value);
    static std::string get_variable(const std::string& name);
};

#endif // BRAHMANDALYM_HPP