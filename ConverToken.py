# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 10:32:54 2020

@author: Mauricio López Benitez

Objetivo1: Generar una lista de token para cada archivo fuente leído 
          en el corpus.


Objetivo 2: Generar lista de trigramas de Token para cada archivo fuente

Salida:  listaNGToken, una lista con las listas de los trigrasmas de token 
         por cada archivo fuente.
"""


import ExtraerPalabras as entrada



#Definición de Tokens en java por medio de un diccionario

def generaToken():
    
    
    
    reservadas={'abstract':'abstract',
                'boolean':'td_boolean',
                'break':'rompeCiclo',
                'byte':'td_byte',
                'byvalue':'byvalue',
                'case':'cond_switch_case',
                'catch':'excep_cacth',
                'char':'td_char',
                'class':'def_clase',
                'const':'def_ctte',
                'cast':'conver_td',
                'operator':'operator',
                'continue':'av_ciclo',
                'default':'metodo_default',
                'do':'do',
                'double':'td_num',
                'else':'else',
                'extends':'extends',
                'false':'val_bool',
                'final':'de_ctte',
                'finally':'finally',
                'float':'td_num',
                'future':'future',
                'outer':'outer',
                'for':'bucle',
                'goto':'goto',
                'if':'condicional',
                'implements':'implements',
                'import':'import',
                'instanceof':'instanceof',
                'int':'td_num',
                'interface':'interface',
                'long':'td_num',
                'native':'native',
                'generic':'generic',
                'rest':'rest',
                'new':'new',
                'null':'null',
                'package':'package',
                'private':'mod_private',
                'protected':'mod_protected',
                'public':'mod_public',
                'return':'retorno',
                'short':'td_num',
                'static':'mod_static',
                'super':'super',
                'inner':'inner',
                'var': 'var',
                'switch':'condicional',
                'synchronized':'synchronized',
                'this':'this',
                'threadsafe':'threadsafe',
                'throw':'throw',
                'throws':'throw',
                'transient':'transient',
                'tru':'val_bool',
                'try':'excep_try',
                'void':'td_void',
                'while':'bucle',
                '?':'condicional'}

    delimitadores= {'(':'p_abre',
                ')':'p_cierra',
                '{':'ll_abre',
                '}':'ll_cierra',
                '[':'c_abre',
                ']':'c_cierra',
                ',':'coma',
                '.':'punto',
                ':':'dosPuntos'
                }

    operadores={'++':'incremento',
            '--':'decremento',
            '+':'incremento',
            '-':'decremento',
            '*':'producto',
            '%':'residuo',
            '/':'division',
            '<':'menorMayor',
                '>':'menorMayor',
            '<=':'menorMayor',
            '>=':'menorMayor',
            '==':'igualdad',
            '!=':'igualdad',
            '=':'asignacion',
            '!':'negacion',
            '&':'and',
            '|':'or',
            '<<':'desplaza',
            '>>':'desplaza',
            '^':'xor'
            }
    
    literalClase ={'add':'add',
        'adddifference':'add',
        'added':'add',
        'addelement':'add',
        'append':'append',
        'appendarray':'append',
        'appendimglist':'append',
        'arraylength':'arraylength',
        'arraylist':'arraylist',
        'arrays':'arraylist',
        'arrchars':'arraylist',
        'as':'as',
        'between':'between',
        'boolexceptionpasswordstestedagain':'boolexceptionpasswordstestedagain',
        'boolexceptionthrown':'boolexceptionthrown',
        'boolfirstlinewritten':'boolfirstlinewritten',
        'boolpasswordfound':'boolpasswordfound',
        'boolreturnvalue':'boolreturnvalue',
        'boolurlisok':'boolurlisok',
        'buffer':'buffer',
        'bufferedinputstream':'bufferedinputstream',
        'bufferedreader':'bufferedreader',
        'bufferedwriter':'bufferedwriter',
        'calendar':'calendar',
        'calfinish':'calfinish',
        'candlength':'candlength',
        'casedpasswords':'casedpasswords',
        'casedscan':'casedscan',
        'catch':'catch',
        'caught':'caught',
        'charat':'charat',
        'check':'check',
        'checkedinputstream':'checkedinputstream',
        'checkfilechanges':'checkfilechanges',
        'checking':'checking',
        'checklastmodified':'checklastmodified',
        'checklastpage':'checklastpage',
        'checkpassword':'checkpassword',
        'classifyimagestodownload':'classifyimagestodownload',
        'clear':'clear',
        'clearallcaches':'clearallcaches',
        'closeserver':'closeserver',
        'closestream':'closestream',
        'compare':'compare',
        'comparediff':'comparediff',
        'comparedigest':'comparedigest',
        'comparefile':'comparefile',
        'compareto':'compareto',
        'comparing':'comparing',
        'comparison':'comparison',
        'concat':'concat',
        'concatenate':'concatenate',
        'connect':'connect',
        'connectionthread':'connectionthread',
        'connectstring':'connectstring',
        'connecturl':'connecturl',
        'connid':'connid',
        'connid,string':'connid,string',
        'connthread':'connthread',
        'connused':'connused',
        'consonantlowerbound':'consonantlowerbound',
        'consonantupperbound':'consonantupperbound',
        'constructemailmessage':'constructemailmessage',
        'constructpassword':'constructpassword',
        'content':'content',
        'convertpassword':'convertpassword',
        'cookie':'cookie',
        'cookiepolicy':'cookiepolicy',
        'copyto':'copyto',
        'copyvalueof':'copyvalueof',
        'create':'create',
        'createcasedpasswords':'createcasedpasswords',
        'createchecksum':'createchecksum',
        'createconnectionthread':'createconnectionthread',
        'createdifffileifneeded':'createdifffileifneeded',
        'createimagetextfile':'createimagetextfile',
        'createnewfile':'createnewfile',
        'createnotesfile':'createnotesfile',
        'createtempfile':'createtempfile',
        'datainputstream':'datainputstream',
        'dataoutputstream':'dataoutputstream',
        'datasource':'datasource',
        'date':'date',
        'decimalformat':'decimalformat',
        'default':'default',
        'deletecharat':'deletecharat',
        'deletefile':'deletefile',
        'deletepage':'deletepage',
        'elementat':'elementat',
        'eof':'eof',
        'equals':'equals',
        'equalsignorecase':'equalsignorecase',
        'err':'err',
        'error':'error',
        'exception':'exception',
        'exit':'exit',
        'fetchlowercase':'fetchlowercase',
        'fetchurl':'fetchurl',
        'fetchword':'fetchword',
        'fetchwords':'fetchwords',
        'file':'file',
        'filenotfoundexception':'filenotfoundexception',
        'fileoutputstream':'fileoutputstream',
        'filepath':'filepath',
        'filereader':'filereader',
        'filetowrite':'filetowrite',
        'filewriter':'filewriter',
        'final':'final',
        'finalize':'finalize',
        'finally':'finally',
        'finalpass':'finalpass',
        'fromaddress':'fromaddress',
        'fromfile':'fromfile',
        'fromserver':'fromserver',
        'fromurl':'fromurl',
        'fullpath':'fullpath',
        'fullscan':'fullscan',
        'getabsolutepath':'getabsolutepath',
        'getaccumulatedlocalattempt':'getaccumulatedlocalattempt',
        'getanykey':'getanykey',
        'getattempts':'getattempts',
        'getattribute':'getattribute',
        'getbasetableindex':'getbasetableindex',
        'getbytearray':'getbytearray',
        'getbytes':'getbytes',
        'getcacheidx':'getcacheidx',
        'getchangemessage':'getchangemessage',
        'getchars':'getchars',
        'getchecksum':'getchecksum',
        'getclass':'getclass',
        'getcommonimages':'getcommonimages',
        'getconnection':'getconnection',
        'getcontent':'getcontent',
        'getdate':'getdate',
        'getdateinstance':'getdateinstance',
        'getdatetimeinstance':'getdatetimeinstance',
        'getdefaultinstance':'getdefaultinstance',
        'getdeletedimages':'getdeletedimages',
        'getdif':'getdif',
        'getdiff':'getdiff',
        'getdifference':'getdifference',
        'getdigestlength':'getdigestlength',
        'getduration':'getduration',
        'getendstr':'getendstr',
        'geterrorstream':'geterrorstream',
        'getfile':'getfile',
        'getfilename':'getfile',
        'getfilesize':'getfile',
        'getflag':'getflag',
        'getfullpath':'getfullpath',
        'getheaderfield':'getheaderfield',
        'gethost':'gethost',
        'gethostconfiguration':'gethost',
        'gethostname':'gethost',
        'geticonheight':'geticonheight',
        'geticonwidth':'geticonwidth',
        'getimage':'getimage',
        'getimagefilename':'getimage',
        'getimageheights':'getimage',
        'getimagename':'getimage',
        'getimagenames':'getimage',
        'getimages':'getimage',
        'getimageslastmodified':'getimage',
        'getimageurl':'getimage',
        'getimagewidths':'getimage',
        'getimgfile':'getimage',
        'getimgheight':'getimage',
        'getimglink':'getimglink',
        'getimglist':'getimglist',
        'getimgnames':'getimgnames',
        'getimgwidth':'getimgwidth',
        'getinputstream':'getinputstream',
        'getinstance':'getinstance',
        'getinterval':'getinterval',
        'getlastmodified':'getlastmodified',
        'getlatest':'getlatest',
        'getlinenumber':'getlinenumber',
        'getlocalattempt':'getlocalattempt',
        'getlocalhost':'getlocalhost',
        'getmailfrom':'getmailfrom',
        'getmailto':'getmailto',
        'getmessage':'getmessage',
        'getmethod':'getmethod',
        'getmethod':'getmethod',
        'getminutes':'getminutes',
        'getmonitorurl':'getmonitorurl',
        'getname':'getname',
        'getnewimages':'getimage',
        'getnewpassword':'getpassword',
        'getnextpassword':'getpassword',
        'getnextstate':'getnextstate',
        'getnumber':'getnumber',
        'getnumberofvariouslengthsofwords':'getnumberofvariouslengthsofwords',
        'getnumofconnections':'getnumofconnections',
        'getoutputstream':'getoutputstream',
        'getoverallattemptpersec':'getoverallattemptpersec',
        'getpage':'getpage',
        'getpagecontents':'getpagecontents',
        'getpassword':'getpassword',
        'getpasswordat':'getpasswordat',
        'getpasswordauthentication':'getpasswordauthentication',
        'getpasswordstried':'getpasswordstried',
        'getpath':'getpath',
        'getport':'getport',
        'getportnumber':'getportnumber',
        'getproperties':'getproperties',
        'getproperty':'getproperty',
        'getprotocol':'getprotocol',
        'getpwdcount':'getpwdcount',
        'getrequestinghost':'getrequestinghost',
        'getrequestingport':'getrequestingport',
        'getrequestingprompt':'getrequestingprompt',
        'getrequestingsite':'getrequestingsite',
        'getresource':'getresource',
        'getresourceasstream':'getresourceasstream',
        'getresponsecode':'getresponsecode',
        'getresponsemessage':'getresponsemessage',
        'getruntime':'getruntime',
        'getseconds':'getseconds',
        'getserverreply':'getserverreply',
        'getsmtpserver':'getsmtpserver',
        'getsource':'getsource',
        'getstartstr':'getstartstr',
        'getstarttime':'getstarttime',
        'getstate':'getstate',
        'getstatus':'getstatus',
        'getstatusline':'getstatusline',
        'getstringinfo':'getstringinfo',
        'getstringw':'getstringw',
        'getstrurl':'getstrurl',
        'getsuccess':'getsuccess',
        'gettime':'gettime',
        'gettimeinmillis':'gettimeinmillis',
        'gettimezone':'gettimezone',
        'gettotaltime':'gettotaltime',
        'geturl':'geturl',
        'getvalue':'getvalue',
        'getvector':'getvector',
        'gif':'gif',
        'givenumberprefix':'givenumberprefix',
        'granted':'granted',
        'gregoriancalendar':'gregoriancalendar',
        'handleconnection':'handleconnection',
        'handlesimpletag':'handlesimpletag',
        'hostname':'hostname',
        'hours':'hours',
        'html':'html',
        'htmldownloaderandimgparser':'htmldownloaderandimgparser',
        'htmleditorkit':'htmleditorkit',
        'http':'http',
        'httpclient':'httpclient',
        'image':'image',
        'include':'include',
        'incommand':'incommand',
        'inputfile':'inputfile',
        'inputstream':'inputstream',
        'inputstreamreader':'inputstreamreader',
        'insertelementat':'insertelementat',
        'instanceof':'instanceof',
        'insuccess':'insuccess',
        'interruptedexception':'interruptedexception',
        'io':'io',
        'ioexception':'ioexception',
        'javax':'javax',
        'joptionpane':'joptionpane',
        'lang':'lang',
        'last':'last',
        'lastfetchidx':'lastfetchidx',
        'lastindexof':'lastindexof',
        'lastlongeststring':'lastlongeststring',
        'lastmodified':'lastmodified',
        'lenght':'lenght',
        'lngfinish':'lngfinish',
        'loadfile':'loadfile',
        'localhost':'localhost',
        'localhost:8080':'localhost:8080',
        'longtimestamp':'longtimestamp',
        'mailto':'mailto',
        'malformedurlexception':'malformedurlexception',
        'match':'match',
        'math':'math',
        'maxchar':'maxchar',
        'maxdiff':'maxdiff',
        'maxdigestfile':'maxdigestfile',
        'maxthread':'maxthread',
        'maxthread>allcombi':'maxthread>allcombi',
        'mkdir':'mkdir',
        'mutableattributeset':'mutableattributeset',
        'newfile':'newfile',
        'nosuchalgorithmexception':'nosuchalgorithmexception',
        'notifyall':'notifyall',
        'now':'now',
        'null':'null',
        'object':'object',
        'observer':'observer',
        'octetstring':'octetstring',
        'open':'open',
        'openconnection':'openconnection',
        'outputstream':'outputstream',
        'password':'password',
        'passwordsize':'passwordsize',
        'passwordstried':'passwordstried',
        'passwordtest':'passwordtest',
        'passwordwasfound':'passwordwasfound',
        'path':'path',
        'performconnection':'performconnection',
        'print':'print',
        'println':'println',
        'read':'read',
        'readcontent':'readcontent',
        'readfile':'readfile',
        'remove':'remove',
        'removeelementat':'removeelementat',
        'replace':'replace',
        'resizearray':'resizearray',
        'return':'return',
        'runtimeexception':'runtimeexception',
        'save':'save',
        'saved':'saved',
        'scantype':'scantype',
        'setdefault':'setdefault',
        'setdoinput':'setdoinput',
        'setdooutput':'setdooutput',
        'setelementat':'setelementat',
        'setfollowredirects':'setfollowredirects',
        'setfrom':'setfrom',
        'sethost':'sethost',
        'setindices':'setindices',
        'settext':'settext',
        'settimetaken':'settimetaken',
        'settimezone':'settimezone',
        'settotaltime':'settotaltime',
        'setusecaches':'setusecaches',
        'showinputdialog':'showinputdialog',
        'simpledateformat':'simpledateformat',
        'simplescan':'simplescan',
        'split':'split',
        'spotdiff':'spotdiff',
        'sql':'sql',
        'src':'src',
        'start':'start',
        'status':'status',
        'stderror':'stderror',
        'stdin':'stdin',
        'stdinput':'stdinput',
        'stdout':'stdout',
        'stdurl':'stdurl',
        'stoptime':'stoptime',
        'storenewfile':'storenewfile',
        'storing':'storing',
        'stream':'stream',
        'strencode':'strencode',
        'strencodeinput':'strencodeinput',
        'strexceptionpassword':'strexceptionpassword',
        'stringbuffer':'stringbuffer',
        'stringtokenizer':'stringtokenizer',
        'stringwriter':'stringwriter',
        'strinputfromfile':'strinputfromfile',
        'strnewcontent':'strnewcontent',
        'strurl':'strurl',
        'substring':'substring',
        'succesfully':'succesfully',
        'success':'success',
        'super':'super',
        'swing':'swing',
        'switch':'switch',
        'synchronized':'synchronized',
        'system':'system',
        'target':'target',
        'testwatchdog':'testwatchdog',
        'text':'text',
        'textarea':'textarea',
        'textdiff':'textdiff',
        'textfilecomparator':'textfilecomparator',
        'textfilename':'textfilename',
        'textmodified':'textmodified',
        'thread':'thread',
        'time':'time',
        'timer':'timer',
        'timezone':'timezone',
        'to':'to',
        'toaddress':'toaddress',
        'toarray':'toarray',
        'tochararray':'tochararray',
        'tofile':'tofile',
        'tokenfile':'tokenfile',
        'tokenizer':'tokenizer',
        'tolowercase':'tolowercase',
        'toserver':'toserver',
        'tostring':'tostring',
        'touppercase':'touppercase',
        'type':'type',
        'unable':'unable',
        'unexpected':'unexpected',
        'unknownhostexception':'unknownhostexception',
        'update':'update',
        'updatecache':'updatecache',
        'url':'url',
        'urlconnection':'url',
        'usage':'use',
        'use':'use',
        'useproxyserver':'useproxyserver',
        'user':'user',
        'username':'user',
        'usr':'user',
        'util':'util',
        'value':'value',
        'valueof':'value',
        'values':'value',
        'vector':'vector',
        'watch':'watch',
        'web':'web'
}

    listaCadena =entrada.identificarPalabras()
    listaToken=[]
    
    for p in listaCadena:
      tokens=[]  
      for i in p:  
        if i in reservadas:
            tokens.append(reservadas[i])
        elif (i in delimitadores):
            tokens.append(delimitadores[i])
        elif (i in operadores):
            tokens.append(operadores[i])
        elif (i in literalClase):
            tokens.append(literalClase[i])
        elif (i=='texto'):
            tokens.append(i)
        elif (i == 'numero'):
            tokens.append(i)
        elif (i=='numeroHx'):
            tokens.append(i)
        else:
            tokens.append('identificador')
      listaToken.append(tokens)
    
   
    return listaToken         
    # for j in range(len(listaToken)):
    #     print("\n"+listaToken[j])
    # #print (listaCadena[0] in operadores)

def nGramaToken():
   
    listaToken=generaToken()
    listaNgToken=[]
      
   
    for tk in listaToken:
        #print("Entro")
        ngToken=[]
    
        for t in range(len(tk)-2):
            ngrama=""
            for i in range(0,3):
                ngrama = ngrama+tk[t+i]
            ngToken.append(ngrama)
        listaNgToken.append(ngToken)
      
  
    #print(listaNgToken[145])
       
    
    
    return listaNgToken
            

#nGramaToken()
        