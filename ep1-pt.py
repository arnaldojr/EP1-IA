"""
  AO PREENCHER ESSE CABECALHO COM O MEU NOME E O MEU NUMERO USP,
  DECLARO QUE SOU A UNICA PESSOA AUTORA E RESPONSAVEL POR ESSE PROGRAMA.
  TODAS AS PARTES ORIGINAIS DESSE EXERCICIO PROGRAMA (EP) FORAM
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUCOES
  DESSE EP E, PORTANTO, NAO CONSTITUEM ATO DE DESONESTIDADE ACADEMICA,
  FALTA DE ETICA OU PLAGIO.
  DECLARO TAMBEM QUE SOU A PESSOA RESPONSAVEL POR TODAS AS COPIAS
  DESSE PROGRAMA E QUE NAO DISTRIBUI OU FACILITEI A
  SUA DISTRIBUICAO. ESTOU CIENTE QUE OS CASOS DE PLAGIO E
  DESONESTIDADE ACADEMICA SERAO TRATADOS SEGUNDO OS CRITERIOS
  DIVULGADOS NA PAGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NAO SERAO CORRIGIDOS E,
  AINDA ASSIM, PODERAO SER PUNIDOS POR DESONESTIDADE ACADEMICA.

  Nome : Arnaldo Alves Viana Junior
  NUSP : 11596396

  Referencias: Com excecao das rotinas fornecidas no enunciado
  e em sala de aula, caso voce tenha utilizado alguma referencia,
  liste-as abaixo para que o seu programa nao seja considerado
  plagio ou irregular.

  Exemplo:
  - O algoritmo Quicksort foi baseado em:
  https://pt.wikipedia.org/wiki/Quicksort
  http://www.ime.usp.br/~pf/algoritmos/aulas/quick.html
  
  Referencias:
  https://jeremykun.com/2012/01/15/word-segmentation/
  https://web.stanford.edu/class/archive/cs/cs221/cs221.1196/assignments/reconstruct/index.html
  http://inst.eecs.berkeley.edu/~cs188/sp20/
"""

import util

############################################################
# Part 1: Segmentation problem under a unigram model

class SegmentationProblem(util.Problem):
    def __init__(self, query, unigramCost):
        self.query = query
        self.unigramCost = unigramCost

    def isState(self, state):
        """ Metodo que implementa verificacao de estado """
        #raise NotImplementedError
        if (state == len(self.query)):
            return True
        else:
            return False

    def initialState(self):
        """ Metodo que implementa retorno da posicao inicial """
        #raise NotImplementedError
        return 0

    def actions(self, state):
        """ Metodo que implementa retorno da lista de acoes validas
        para um determinado estado
        """
        # raise NotImplementedError
        word = self.query[state:]
        action = [word[:i] for i in range(1,len(word) + 1)]
        #print("action", action)
        return action


    def nextState(self, state, action):
        """ Metodo que implementa funcao de transicao """
        #raise NotImplementedError
        nextstate = state + len(action)
        return nextstate


    def isGoalState(self, state):
        """ Metodo que implementa teste de meta """
        #raise NotImplementedError
        if (state == len(self.query)):
            return True
        else:
            return False

    def stepCost(self, state, action):
        """ Metodo que implementa funcao custo """
        #raise NotImplementedError
        stepcost = self.unigramCost(action)
        if state != self.initialState:
            return stepcost

def segmentWords(query, unigramCost):

    if len(query) == 0:
        return ''
    else:
    # BEGIN_YOUR_CODE 
    # Voce pode usar a função getSolution para recuperar a sua solução a partir do no meta
    # valid,solution  = util.getSolution(goalNode,problem)
    # raise NotImplementedError
        problem = SegmentationProblem(query, unigramCost)
        goal = util.uniformCostSearch(problem)
        valid, solution  = util.getSolution(goal,problem)
        return solution
    # END_YOUR_CODE


############################################################
# Part 2: Vowel insertion problem under a bigram cost

class VowelInsertionProblem(util.Problem):
    def __init__(self, queryWords, bigramCost, possibleFills):
        self.queryWords = queryWords
        self.bigramCost = bigramCost
        self.possibleFills = possibleFills

    def isState(self, state):
        """ Metodo  que implementa verificacao de estado """
        # raise NotImplementedError
        return

    def initialState(self):
        """ Metodo  que implementa retorno da posicao inicial """
        #raise NotImplementedError
        self.queryWords.insert(0,util.SENTENCE_BEGIN)
        # result = self.queryWords #tem que ser tuple tem dicionario em util
        result = tuple(self.queryWords,) 
        # print("initialState: ",result) 
        return result

    def actions(self, state):
        """ Metodo  que implementa retorno da lista de acoes validas
        para um determinado estado
        """
        # raise NotImplementedError
        # print("o que é possibleFills:", self.possibleFills)
        # print("o que é possibleFills:", self.queryWords)
        acao = []
        # for i in range(0, len(state)):
        #     print(state[i])
        #     possiblefill = self.possibleFills(state[i])
        #     for j in possiblefill:
        #         acao.append((j,i))
        acao = [(j,i) for i in range(0, len(state)) for j in self.possibleFills(state[i]) ]
        # print("acoes: ",acao)
        return acao

    def nextState(self, state, action):
        """ Metodo que implementa funcao de transicao """
        # raise NotImplementedError
        # print("o que é state:", state)
        # print("o que é action:", action)
        nextstate = action 
        return nextstate

    def isGoalState(self, state):
        """ Metodo que implementa teste de meta """
        # raise NotImplementedError
        # print("action(state): ", self.actions(state))
        if self.actions(state) != []:
            # print("estadometa: ", False)
            return False
        # print("estadometa: ", True)
        return True

    def stepCost(self, state, action):
        """ Metodo que implementa funcao custo """
        # raise NotImplementedError
        cost = 0
        for i in range(len(action)-1):
            cost += self.bigramCost(action[i], action[i+1])
        return cost



def insertVowels(queryWords, bigramCost, possibleFills):
    # BEGIN_YOUR_CODE 
    # Voce pode usar a função getSolution para recuperar a sua solução a partir do no meta
    # valid,solution  = util.getSolution(goalNode,problem)
    #  raise NotImplementedError
    problem = VowelInsertionProblem(queryWords, bigramCost, possibleFills)
    goal = util.uniformCostSearch(problem)
    valid, solution  = util.getSolution(goal,problem)

    if valid:
        return goal.state
    return result
    # END_YOUR_CODE


############################################################


def getRealCosts(corpus='corpus.txt'):

    """ Retorna as funcoes de custo unigrama, bigrama e possiveis fills obtidas a partir do corpus."""
    
    _realUnigramCost, _realBigramCost, _possibleFills = None, None, None
    if _realUnigramCost is None:
        print('Training language cost functions [corpus: '+ corpus+']... ')
        
        _realUnigramCost, _realBigramCost = util.makeLanguageModels(corpus)
        _possibleFills = util.makeInverseRemovalDictionary(corpus, 'aeiou')

        print('Done!')

    return _realUnigramCost, _realBigramCost, _possibleFills

def getRealCostspt(corpus='corpuspt.txt'):

    """ Retorna as funcoes de custo unigrama, bigrama e possiveis fills obtidas a partir do corpus em portugues."""
    
    _realUnigramCost, _realBigramCost, _possibleFills = None, None, None
    if _realUnigramCost is None:
        print('Treinamento em portugues do custo da funcão [corpus: '+ corpus+']... ')
        
        _realUnigramCost, _realBigramCost = util.makeLanguageModels(corpus)
        _possibleFills = util.makeInverseRemovalDictionary(corpus, 'aeiou')

        print('Done!')

    return _realUnigramCost, _realBigramCost, _possibleFills


def main():
    """ Voce pode/deve editar o main() para testar melhor sua implementacao.

    A titulo de exemplo, incluimos apenas algumas chamadas simples para
    lhe dar uma ideia de como instanciar e chamar suas funcoes.
    Descomente as linhas que julgar conveniente ou crie seus proprios testes.
    """
    # frase = 'believeinyour'
    # unigramCost, bigramCost, possibleFills  =  getRealCosts()
    
   
    ##############################################################################
    # Para testar com frases em portugues, usar a funcao getRealCostspt() abaixo #
    ##############################################################################   
    frase = 'voceconsegueterminarestetrabalho'
    unigramCost, bigramCost, possibleFills  =  getRealCostspt()
    
    
    
    resulSegment = segmentWords(frase, unigramCost)   
    print("frase:",frase)
    print("resultado:",resulSegment)

    
    # resultInsert = insertVowels('smtms ltr bcms nvr'.split(), bigramCost, possibleFills)
    # print(resultInsert)

if __name__ == '__main__':
    main()
