import sys
question_input = sys.argv[1]
import wolframalpha
import ssl
import requests
import wikipedia
question_input = sys.argv[1]
try:
    def wiki_search(vinput):
        wiki_result = wikipedia.search(vinput)
        if not wiki_result:
            print("no results from wikipedia")
            return
        try:
            page = wikipedia.page(searchResults[0])
            print(page)
        except:
            print("error occured while searching wikipedia")

    def wolfram_search(vinput):
        client = wolframalpha.Client("UE63QU-6YE6GKLHJU")
        res = client.query(vinput)
        if res['@success'] == 'false':
            print("question cannot be resolved by wolfram alpha")
        else:
            result = ''
            #pod[0] = question
            pod0 = res['pod'][0]
            #pod[1] = answer
            pod1 = res['pod'][1]
            if (('definition' in pod1['@title'].lower()) or ('result' in  pod1['@title'].lower()) or (pod1.get('@primary','false') == 'true')):
                result = resolveListOrDict(pod1['subpod'])
                #file.write(result)
                print(result)
            else:
                question = resolveListOrDict(pod0['subpod']) #gets wolframs question interpritation
                question = removeBrackets(question)
                wiki_search(question)

    def resolveListOrDict(variable):
      if isinstance(variable, list):
        return variable[0]['plaintext']
      else:
        return variable['plaintext']

    def removeBrackets(variable):
      return variable.split('(')[0]

    vinput = question_input
    wolfram_search(vinput)
except:
    print("\n unknown error in executing python file")

