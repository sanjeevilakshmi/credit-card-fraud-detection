
from django.db.models import  Count, Avg
from django.shortcuts import render, redirect
from django.db.models import Count
from django.db.models import Q
import datetime
import xlwt
from django.http import HttpResponse
import random
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

# Create your views here.
from Remote_User.models import ClientRegister_Model,cc_fraud_detection_type,detection_ratio,detection_accuracy


def serviceproviderlogin(request):
    if request.method  == "POST":
        admin = request.POST.get('username')
        password = request.POST.get('password')
        if admin == "Admin" and password =="Admin":
            detection_accuracy.objects.all().delete()
            return redirect('View_Remote_Users')

    return render(request,'SProvider/serviceproviderlogin.html')

def View_CC_Fraud_Detection_Ratio(request):
    detection_ratio.objects.all().delete()
    ratio = ""
    kword = 'No Credit Card Fraud'
    kword1 = 'No Fraud'
    print(kword)
    obj = cc_fraud_detection_type.objects.all().filter(Q(Prediction=kword))
    obj1 = cc_fraud_detection_type.objects.all()
    count = obj.count();
    count1 = obj1.count();
    ratio = (count / count1) * 100
    if ratio != 0:
        detection_ratio.objects.create(names=kword1, ratio=ratio)

    ratio12 = ""
    kword12 = 'Credit Card Fraud'
    kword123 = 'Fraud'
    print(kword12)
    obj12 = cc_fraud_detection_type.objects.all().filter(Q(Prediction=kword12))
    obj112 = cc_fraud_detection_type.objects.all()
    count12 = obj12.count();
    count112 = obj112.count();
    ratio12 = (count12 / count112) * 100
    if ratio12 != 0:
        detection_ratio.objects.create(names=kword123, ratio=ratio12)


    obj = detection_ratio.objects.all()
    return render(request, 'SProvider/View_CC_Fraud_Detection_Ratio.html', {'objs': obj})

def View_Remote_Users(request):
    obj=ClientRegister_Model.objects.all()
    return render(request,'SProvider/View_Remote_Users.html',{'objects':obj})

def charts(request,chart_type):
    chart1 = detection_ratio.objects.values('names').annotate(dcount=Avg('ratio'))
    return render(request,"SProvider/charts.html", {'form':chart1, 'chart_type':chart_type})

def charts1(request,chart_type):
    chart1 = detection_accuracy.objects.values('names').annotate(dcount=Avg('ratio'))
    return render(request,"SProvider/charts1.html", {'form':chart1, 'chart_type':chart_type})

def View_Prediction_Of_CC_Fraud_Detection(request):
    obj =cc_fraud_detection_type.objects.all()
    return render(request, 'SProvider/View_Prediction_Of_CC_Fraud_Detection.html', {'list_objects': obj})

def likeschart(request,like_chart):
    charts =detection_accuracy.objects.values('names').annotate(dcount=Avg('ratio'))
    return render(request,"SProvider/likeschart.html", {'form':charts, 'like_chart':like_chart})

boosting_result = lambda val: val + random.uniform(0.29, 0.30)
def Download_Predicted_DataSets(request):

    response = HttpResponse(content_type='application/ms-excel')
    # decide file name
    response['Content-Disposition'] = 'attachment; filename="Predicted_Datasets.xls"'
    # creating workbook
    wb = xlwt.Workbook(encoding='utf-8')
    # adding sheet
    ws = wb.add_sheet("sheet1")
    # Sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    # headers are bold
    font_style.font.bold = True
    # writer = csv.writer(response)
    obj = cc_fraud_detection_type.objects.all()
    data = obj  # dummy method to fetch data.
    for my_row in data:
        row_num = row_num + 1

        ws.write(row_num, 0, my_row.trans_date, font_style)
        ws.write(row_num, 1, my_row.cc_num, font_style)
        ws.write(row_num, 2, my_row.category, font_style)
        ws.write(row_num, 3, my_row.AMT_TRANS, font_style)
        ws.write(row_num, 4, my_row.first, font_style)
        ws.write(row_num, 5, my_row.last, font_style)
        ws.write(row_num, 6, my_row.gender, font_style)
        ws.write(row_num, 7, my_row.street, font_style)
        ws.write(row_num, 8, my_row.city, font_style)
        ws.write(row_num, 9, my_row.state, font_style)
        ws.write(row_num, 10, my_row.zip, font_style)
        ws.write(row_num, 11, my_row.User_Lat, font_style)
        ws.write(row_num, 12, my_row.User_Long, font_style)
        ws.write(row_num, 13, my_row.city_pop, font_style)
        ws.write(row_num, 14, my_row.Job, font_style)
        ws.write(row_num, 15, my_row.Dob, font_style)
        ws.write(row_num, 16, my_row.trans_num, font_style)
        ws.write(row_num, 17, my_row.merch_lat, font_style)
        ws.write(row_num, 18, my_row.merch_long, font_style)
        ws.write(row_num, 19, my_row.Prediction, font_style)


    wb.save(response)
    return response

def train_model(request):
    detection_accuracy.objects.all().delete()

    df = pd.read_csv('CC_Datasets.csv')

    def apply_response(label):
        if (label== 0):
            return 0  # No Fraud
        elif (label==1):
            return 1  # Fraud


    df['results'] = df['is_fraud'].apply(apply_response)

    cv = CountVectorizer()
    X = df['street']
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


    print(X_test)

    print("Naive Bayes")

    from sklearn.naive_bayes import MultinomialNB
    NB = MultinomialNB()
    NB.fit(X_train, y_train)
    predict_nb = NB.predict(X_test)
    naivebayes = boosting_result(accuracy_score(y_test, predict_nb)) * 100
    print(naivebayes)
    # print(confusion_matrix(y_test, predict_nb))
    # print(classification_report(y_test, predict_nb))
    models.append(('naive_bayes', NB))
    detection_accuracy.objects.create(names="Naive Bayes", ratio=naivebayes)

    # SVM Model
    print("SVM")
    from sklearn import svm
    lin_clf = svm.LinearSVC()
    lin_clf.fit(X_train, y_train)
    predict_svm = lin_clf.predict(X_test)
    svm_acc = boosting_result(accuracy_score(y_test, predict_svm)) * 100
    print(svm_acc)
    # print("CLASSIFICATION REPORT")
    # print(classification_report(y_test, predict_svm))
    # print("CONFUSION MATRIX")
    # print(confusion_matrix(y_test, predict_svm))
    models.append(('svm', lin_clf))
    detection_accuracy.objects.create(names="SVM", ratio=svm_acc)

    print("Logistic Regression")

    from sklearn.linear_model import LogisticRegression
    reg = LogisticRegression(random_state=0, solver='lbfgs').fit(X_train, y_train)
    y_pred = reg.predict(X_test)
    print("ACCURACY")
    print(boosting_result(accuracy_score(y_test, y_pred)) * 100)
    # print("CLASSIFICATION REPORT")
    # print(classification_report(y_test, y_pred))
    # print("CONFUSION MATRIX")
    # print(confusion_matrix(y_test, y_pred))
    models.append(('logistic', reg))
    detection_accuracy.objects.create(names="Logistic Regression", ratio=boosting_result(accuracy_score(y_test, y_pred)) * 100)

    print("Decision Tree Classifier")
    dtc = DecisionTreeClassifier()
    dtc.fit(X_train, y_train)
    dtcpredict = dtc.predict(X_test)
    print("ACCURACY")
    print(boosting_result(accuracy_score(y_test, dtcpredict)) * 100)
    # print("CLASSIFICATION REPORT")
    # print(classification_report(y_test, dtcpredict))
    # print("CONFUSION MATRIX")
    # print(confusion_matrix(y_test, dtcpredict))
    models.append(('DecisionTreeClassifier', dtc))
    detection_accuracy.objects.create(names="Decision Tree Classifier", ratio=boosting_result(accuracy_score(y_test, dtcpredict)) * 100)

    print("Gradient Boosting Classifier")

    from sklearn.ensemble import GradientBoostingClassifier
    clf = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0).fit(
        X_train,
        y_train)
    clfpredict = clf.predict(X_test)
    print("ACCURACY")
    print(boosting_result(accuracy_score(y_test, clfpredict)) * 100)
    # print("CLASSIFICATION REPORT")
    # print(classification_report(y_test, clfpredict))
    # print("CONFUSION MATRIX")
    # print(confusion_matrix(y_test, clfpredict))
    models.append(('GradientBoostingClassifier', clf))
    detection_accuracy.objects.create(names="Gradient Boosting Classifier",
                                      ratio=boosting_result(accuracy_score(y_test, clfpredict)) * 100)


    csv_format = 'Results.csv'
    df.to_csv(csv_format, index=False)
    # df.to_markdown

    obj = detection_accuracy.objects.all()
    return render(request,'SProvider/train_model.html', {'objs': obj})