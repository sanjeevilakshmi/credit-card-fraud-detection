from django.db.models import Count
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
# Create your views here.
from Remote_User.models import ClientRegister_Model,cc_fraud_detection_type,detection_ratio,detection_accuracy

def login(request):


    if request.method == "POST" and 'submit1' in request.POST:

        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            enter = ClientRegister_Model.objects.get(username=username,password=password)
            request.session["userid"] = enter.id

            return redirect('ViewYourProfile')
        except:
            pass

    return render(request,'RUser/login.html')

def index(request):
    return render(request, 'RUser/index.html')

def Add_DataSet_Details(request):

    return render(request, 'RUser/Add_DataSet_Details.html', {"excel_data": ''})


def Register1(request):

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phoneno = request.POST.get('phoneno')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        ClientRegister_Model.objects.create(username=username, email=email, password=password, phoneno=phoneno,
                                            country=country, state=state, city=city,address=address,gender=gender)

        obj = "Registered Success"
        return render(request, 'RUser/Register1.html',{'object':obj})
    else:
        return render(request,'RUser/Register1.html')

def ViewYourProfile(request):
    userid = request.session['userid']
    obj = ClientRegister_Model.objects.get(id= userid)
    return render(request,'RUser/ViewYourProfile.html',{'object':obj})


def Predict_Credit_Card_Fraud_Detection(request):
    if request.method == "POST":

        if request.method == "POST":

            trans_date= request.POST.get('trans_date')
            cc_num= request.POST.get('cc_num')
            category= request.POST.get('category')
            AMT_TRANS= request.POST.get('AMT_TRANS')
            first= request.POST.get('first')
            last= request.POST.get('last')
            gender= request.POST.get('gender')
            street= request.POST.get('street')
            city= request.POST.get('city')
            state= request.POST.get('state')
            zip= request.POST.get('zip')
            User_Lat= request.POST.get('User_Lat')
            User_Long= request.POST.get('User_Long')
            city_pop= request.POST.get('city_pop')
            Job= request.POST.get('Job')
            Dob= request.POST.get('Dob')
            trans_num= request.POST.get('trans_num')
            merch_lat= request.POST.get('merch_lat')
            merch_long= request.POST.get('merch_long')

        df = pd.read_csv('CC_Datasets.csv')

        def apply_response(label):
            if (label == 0):
                return 0  # No Fraud
            elif (label == 1):
                return 1  # Fraud
        df['results'] = df['is_fraud'].apply(apply_response)

        cv = CountVectorizer()
        X = df['trans_num']
        y = df['results']

        print("Transaction Number")
        print(X)
        print("Results")
        print(y)

        X = cv.fit_transform(X)

        models = []
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
        X_train.shape, X_test.shape, y_train.shape

        print("Naive Bayes")

        from sklearn.naive_bayes import MultinomialNB

        NB = MultinomialNB()
        NB.fit(X_train, y_train)
        predict_nb = NB.predict(X_test)
        naivebayes = accuracy_score(y_test, predict_nb) * 100
        print("ACCURACY")
        print(naivebayes)
        print("CLASSIFICATION REPORT")
        print(classification_report(y_test, predict_nb))
        print("CONFUSION MATRIX")
        print(confusion_matrix(y_test, predict_nb))
        models.append(('naive_bayes', NB))

        # SVM Model
        print("SVM")
        from sklearn import svm

        lin_clf = svm.LinearSVC()
        lin_clf.fit(X_train, y_train)
        predict_svm = lin_clf.predict(X_test)
        svm_acc = accuracy_score(y_test, predict_svm) * 100
        print("ACCURACY")
        print(svm_acc)
        print("CLASSIFICATION REPORT")
        print(classification_report(y_test, predict_svm))
        print("CONFUSION MATRIX")
        print(confusion_matrix(y_test, predict_svm))
        models.append(('svm', lin_clf))

        print("Logistic Regression")

        from sklearn.linear_model import LogisticRegression

        reg = LogisticRegression(random_state=0, solver='lbfgs').fit(X_train, y_train)
        y_pred = reg.predict(X_test)
        print("ACCURACY")
        print(accuracy_score(y_test, y_pred) * 100)
        print("CLASSIFICATION REPORT")
        print(classification_report(y_test, y_pred))
        print("CONFUSION MATRIX")
        print(confusion_matrix(y_test, y_pred))
        models.append(('logistic', reg))


        classifier = VotingClassifier(models)
        classifier.fit(X_train, y_train)
        y_pred = classifier.predict(X_test)

        trans_num1 = [trans_num]
        vector1 = cv.transform(trans_num1).toarray()
        predict_text = classifier.predict(vector1)

        pred = str(predict_text).replace("[", "")
        pred1 = pred.replace("]", "")

        prediction = int(pred1)

        if (prediction == 0):
            val = 'NO Fraud Detected'
        elif (prediction == 1):
            val = 'Fraud Detected'

        print(val)
        print(pred1)

        cc_fraud_detection_type.objects.create(
        trans_date=trans_date,
        cc_num=cc_num,
        category=category,
        AMT_TRANS=AMT_TRANS,
        first=first,
        last=last,
        gender=gender,
        street=street,
        city=city,
        state=state,
        zip=zip,
        User_Lat=User_Lat,
        User_Long=User_Long,
        city_pop=city_pop,
        Job=Job,
        Dob=Dob,
        trans_num=trans_num,
        merch_lat=merch_lat,
        merch_long=merch_long,
        Prediction=val)

        return render(request, 'RUser/Predict_Credit_Card_Fraud_Detection.html',{'objs': val})
    return render(request, 'RUser/Predict_Credit_Card_Fraud_Detection.html')



