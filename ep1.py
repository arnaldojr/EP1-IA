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
  
  https://jeremykun.com/2012/01/15/word-segmentation/
  https://web.stanford.edu/class/archive/cs/cs221/cs221.1196/assignments/reconstruct/index.html

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


    def initialState(self):
        """ Metodo  que implementa retorno da posicao inicial """
        #raise NotImplementedError
        self.queryWords.insert(0,util.SENTENCE_BEGIN)
        result = tuple(self.queryWords,) #tem que ser tuple
        print("initialState: ",result) 
        return result

    def actions(self, state):
        """ Metodo  que implementa retorno da lista de acoes validas
        para um determinado estado
        """
        # raise NotImplementedError

    def nextState(self, state, action):
        """ Metodo que implementa funcao de transicao """
        # raise NotImplementedError

    def isGoalState(self, state):
        """ Metodo que implementa teste de meta """
        # raise NotImplementedError

    def stepCost(self, state, action):
        """ Metodo que implementa funcao custo """
        # raise NotImplementedError



def insertVowels(queryWords, bigramCost, possibleFills):
    # BEGIN_YOUR_CODE 
    # Voce pode usar a função getSolution para recuperar a sua solução a partir do no meta
    # valid,solution  = util.getSolution(goalNode,problem)
    #  raise NotImplementedError
    problem = VowelInsertionProblem(queryWords, bigramCost, possibleFills)
    goal = util.uniformCostSearch(problem)
    # valid, solution = util.getSolution(goal, problem)

    # if valid:
    #     return solution

    # return None



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

def main():
    """ Voce pode/deve editar o main() para testar melhor sua implementacao.

    A titulo de exemplo, incluimos apenas algumas chamadas simples para
    lhe dar uma ideia de como instanciar e chamar suas funcoes.
    Descomente as linhas que julgar conveniente ou crie seus proprios testes.
    """
    unigramCost, bigramCost, possibleFills  =  getRealCosts()
    
    # frase = 'mynameis'
    # frase = 'believeinyour'
    # frase = 'believeinyourselfhavefaithinyourabilities'
    # frase = 'believeinyourselfhavefaithinyourabilitiesbelieveinyourselfhavefaithinyourabilitiesbelieveinyourselfhavefaithinyourabilitiesbelieveinyourselfhavefaithinyourabilitiesbelieveinyourselfhavefaithinyourabilitiesbelieveinyourselfhavefaithinyourabilitiesbelieveinyourselfhavefaithinyourabilitiesbelieveinyourselfhavefaithinyourabilitiesbelieveinyourselfhavefaithinyourabilitiesbelieveinyourselfhavefaithinyourabilitiesbelieveinyourselfhavefaithinyourabilitiesbelieveinyourselfhavefaithinyourabilitiesbelieveinyourselfhavefaithinyourabilitiesbelieveinyourselfhavefaithinyourabilitiesbelieveinyourselfhavefaithinyourabilitiesbelieveinyourselfhavefaithinyourabilitiesbelieveinyourselfhavefaithinyourabilitiesbelieveinyourselfhavefaithinyourabilitiesbelieveinyourselfhavefaithinyourabilitiesbelieveinyourselfhavefaithinyourabilitiesbelieveinyourselfhavefaithinyourabilitiesbelieveinyourselfhavefaithinyourabilitiesbelieveinyourselfhavefaithinyourabilitiesbelieveinyourselfhavefaithinyourabilitiesbelieveinyourselfhavefaithinyourabilitiesbelieveinyourselfhavefaithinyourabilitiesbelieveinyourselfhavefaithinyourabilitiesbelieveinyourselfhavefaithinyourabilitiesbelieveinyourselfhavefaithinyourabilitiesbelieveinyourselfhavefaithinyourabilitiesbelieveinyourselfhavefaithinyourabilitiesbelieveinyourselfhavefaithinyourabilitiesbelieveinyourselfhavefaithinyourabilitiesbelieveinyourselfhavefaithinyourabilitiesbelieveinyourselfhavefaithinyourabilitiesbelieveinyourselfhavefaithinyourabilitiesbelieveinyourselfhavefaithinyourabilitiesbelieveinyourselfhavefaithinyourabilitiesbelieveinyourselfhavefaithinyourabilitiesbelieveinyourselfhavefaithinyourabilitiesbelieveinyourselfhavefaithinyourabilities'    
    # resulSegment = segmentWords(frase, unigramCost)
    # resulSegment = segmentWords('believeinyour', unigramCost)
    # print("frase:",frase)
    # print("resultado:",resulSegment)
    
    resultInsert = insertVowels('smtms ltr bcms nvr'.split(), bigramCost, possibleFills)
    print(resultInsert)

if __name__ == '__main__':
    main()
