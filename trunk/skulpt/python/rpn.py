import math
class Infix2Rpn:
  def __init__(self, equ):
    self.stack = []
    self.tokens = self.infix2tokens(equ)
    self.rpn = self.tokens2postfix(self.tokens)
    self.rpn_str = ' '.join(self.rpn)
  
  def update(self, equ):
    self.stack = []
    self.tokens = self.infix2tokens(equ)
    self.rpn = self.tokens2postfix(self.tokens)
    self.rpn_str = ' '.join(self.rpn)
  
    
  def push_stack(self,x): 
    self.stack.append(x) 
  def pop_stack(self): 
    return self.stack.pop() 
  def top_stack(self): 
    return(self.stack[len(self.stack)-1]) 
  def is_empty(self): 
    if(len(self.stack) == 0): 
        return 1 
    return 0 
  def is_unaryoperator(self,x): 
    if (x.lower() == "sqrt" or
            x.lower() == "not" or 
            x.lower() == "exp" or    
            x.lower() == "ln" or    
            x.lower() == "log" or    
            x.lower() == "sin" or 
            x.lower() == "cos" or    
            x.lower() == "tan" or    
            x.lower() == "arcsin" or    
            x.lower() == "arccos" or    
            x.lower() == "arctan"): 
        return 1 
    return 0 
  def is_binaryoperator(self,x): 
    if (x == "+" or    
            x == "&" or 
            x == "|" or 
            x == "-" or    
            x == "*" or    
            x == "/" or    
            x == "^"): 
        return 1 
    return 0 
  def is_operand(self,x): 
    if (not(self.is_unaryoperator(x)) and    
            not(self.is_binaryoperator(x)) and    
            x != "(" and    
            x != ")"): 
        return 1 
    return 0 
  def precedence(self,x): 
    if(x == "^"): 
        return(5) 
    if((x == "*") or (x == "/") or (x == "&")): 
        return(4) 
    if((x == "+") or (x == "-")) or (x == "|"): 
        return(3) 
    if(x == "("): 
        return(2) 
    if(x == ")"): 
        return(1) 
  def infix2tokens(self,infixStr): 
    tempStr = "" 
    tokensStr = [] 
    count = 0 
    for x in infixStr: 
        count += 1 
        if x != " ": 
            if(self.is_operand(x)): 
                tempStr += x 
            if(self.is_binaryoperator(x) or 
                     x == ")" or x == "("):
                        
                if(tempStr != ""): 
                    tokensStr.append(tempStr) 
                tempStr = "" 
                tokensStr.append(x) 
        if(count == len(infixStr)): 
            if(tempStr != ""): 
                tokensStr.append(tempStr) 
    return(tokensStr)

  def tokens2postfix(self,tokensStr,postfixStr = []): 
    self.stack = [] 
    postfixStr = [] 
    for x in tokensStr: 
        if(self.is_operand(x)): 
            postfixStr.append(x) 
        if(self.is_unaryoperator(x)): 
            self.push_stack(x) 
        if(self.is_binaryoperator(x)): 
            if(x != "^"): 
                while((not(self.is_empty())) and 
                            (self.precedence(x) <= self.precedence(self.top_stack()))): 
                    postfixStr.append(self.top_stack()) 
                    self.pop_stack() 
            else: 
                while((not(self.is_empty())) and 
                            (self.precedence(x) < self.precedence(self.top_stack()))): 
                    postfixStr.append(self.top_stack()) 
                    self.pop_stack(self.stack) 
            self.push_stack(x) 
        if(x == "("): 
            self.push_stack(x) 
        if(x == ")"): 
            while(self.top_stack() != "("): 
                postfixStr.append(self.pop_stack()) 
            self.pop_stack() 
            if not(self.is_empty()): 
                if (self.is_unaryoperator(self.top_stack())): 
                    postfixStr.append(self.pop_stack()) 
    while(not(self.is_empty())): 
        if(self.top_stack() == "("): 
            self.pop_stack() 
        else: 
            postfixStr.append(self.pop_stack()) 
    return(postfixStr) 

class RpnMathParser:
    def __init__(self, equ, vars = {}):
        self.ops = {
            'not': self.op_neg, 
            '&': self.op_and, 
            '|': self.op_or, 
            '^': self.op_pow,
            '*': self.op_mul,
            '/': self.op_div,
            '+': self.op_add,
            '-': self.op_sub,
            'sin': self.op_sin,
            'cos': self.op_cos,
           'sqrt': self.op_sqrt,
        }
        self.stack = []
        self.vars = vars
        self.equation = "".join(equ.split(" "))
        
        print self.equation
        
        self.equation = self.equation.replace("(-","(0-")
        self.equation = self.equation.replace("++","+")
        self.equation = self.equation.replace("--","+")
        self.equation = self.equation.replace("-+","-")
        self.equation = self.equation.replace("+-","-")
        
        self.converter = Infix2Rpn(self.equation)
        compute = self.rpn_calc()
        self.result = compute[-1][2]
        #print self.result

    def update(self, simul_var=[], simul_val = []):
        
        results=[]
        #print simul_var, simul_val, len(simul_val)
        for j in range(len(simul_val)):
            equ = self.equation     
            for i in range(len(simul_var)):
                equ = equ.replace(simul_var[i], str(simul_val[j][i]))
                #print j,i,equ,simul_var[i], simul_val[j][i]
                if i == len(simul_var)-1:
                    #print "update"
                    self.stack = []
                    self.converter.update(equ)
                    #print equ, self.converter.rpn_str
                    compute = self.rpn_calc(False)
                    tab = compute[-1][2].split(" ")
                    results.append(tab[-1])
        return results
  
    def op_neg(self):
        b = self.stack.pop()
        self.stack.append((b+1) % 2)
    def op_and(self):
        b = self.stack.pop(); a = self.stack.pop()
        self.stack.append((a and b) % 2)
    def op_or(self):
        b = self.stack.pop(); a = self.stack.pop()
        self.stack.append((a or b) % 2)     
    def op_sqrt(self):
        b = self.stack.pop()
        self.stack.append(math.sqrt(b))
    def op_sin(self):
        b = self.stack.pop()
        self.stack.append(math.sin(b))
    def op_cos(self):
        b = self.stack.pop()
        self.stack.append(math.cos(b))
    def op_pow(self):
        b = self.stack.pop(); a = self.stack.pop()
        self.stack.append( a ** b )
    def op_mul(self):
        b = self.stack.pop(); a = self.stack.pop()
        self.stack.append( a * b )
    def op_div(self):
        b = self.stack.pop(); 
        a = self.stack.pop()
        self.stack.append( a / b )
    def op_add(self):
        b = self.stack.pop(); a = self.stack.pop()
        self.stack.append( a + b )
    def op_sub(self):
        b = self.stack.pop()
        if len(self.stack) == 0:
            self.stack.append(0)
        a = self.stack.pop()
        self.stack.append( a - b )
    def op_num(self, num):
        self.stack.append( num )
 
    def print_result(self):
        print self.result
    def get_result(self):
        return self.result
 
    def get_input(self):
        'Inputs an expression and returns list of tokens'
 
        tokens = inp.strip().split()
        return tokens
    
    def rpn_calc(self, empty = True):
        if empty:
            self.stack = []
        tokens = self.converter.rpn_str.split(' ')
        #print "RPN: ", tokens
        table = ['TOKEN,ACTION,STACK'.split(',')]
        for token in tokens:
                if token in self.ops:
                        action = 'Apply op to top of self.stack'
                        self.ops[token]()
                        table.append( (token, action, ' '.join(str(s) for s in self.stack)) )
                else:
                        action = 'Push num onto top of self.stack'
                        if self.vars.has_key(token):
                            token = self.vars[token]
                        else:
                            if token == "not1":
                                token="0"
                            if token == "not0":
                                token="1"
                        self.op_num(float(token))
                        table.append((token, action, ' '.join(str(s) for s in self.stack)))
        return table
 
 
if __name__ == '__main__':
    
    variables = {'a': 0, 'b': 0}
    simul_var = ['a','b']
    simul_val = [[0,0],[0,1],[1,0],[1,1]]

    equations = [
                 "-cos(a)","a","not(a)","a & b","a | b",
                 "not(a & b)", "not(a | b)",
                 "not(a) & b | not(b) & a",
                 "not(a) & not(b) | b & a"
                 ]
    
    for eq in equations:
        print eq
        parser = RpnMathParser(eq, variables); 
        parser.print_result()
        results = parser.update(simul_var,simul_val); 
        print results
