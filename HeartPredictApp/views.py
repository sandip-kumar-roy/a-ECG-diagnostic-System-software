from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from HeartPredictApp.models import predict_form
from django.http import HttpResponseRedirect
import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
#created a reference object 
model = joblib.load("trained_model.sav")
pred_obj=predict_form()
def prdictformpage(request):
    if request.user.is_authenticated:
        return render(request,'predictionform.html')
    else:
        return render(request,'login.html',{"warn":"Login to Your Account In order To use our Prediction Tool!!!"})

def reg(request):
    return HttpResponseRedirect('register')   


def result_page(request):
    if request.method=="POST":
        age=int(request.POST["age"])
        Chest_pain_type=request.POST["cpt"]
        resting_blood_pressure=request.POST["rbp"]
        serum_cholestoral=request.POST["sc"]
        fasting_blood_sugar=(request.POST["fbs"])
        resting_electrocardiographic=(request.POST["re"])
        max_heart_rate=int(request.POST["mhr"])
        exercise_induced_angina=(request.POST["eia"])
        oldpeak=float(request.POST["op"])
        peak_ST_segment_slope=(request.POST["peakst"])
        major_vessels=int(request.POST["mv"])
        thal=(request.POST["thal"])
        gen=request.POST["gender"]
        current_user=request.user
        print(current_user)
        pred_obj=predict_form(
            user_name=current_user.username,
            age=age,
            Chest_pain_type=Chest_pain_type,
            resting_blood_pressure=resting_blood_pressure,
            serum_cholestoral=serum_cholestoral,
            fasting_blood_sugar=fasting_blood_sugar,
            resting_electrocardiographic=resting_electrocardiographic,
            max_heart_rate=max_heart_rate,
            exercise_induced_angina=exercise_induced_angina,
            oldpeak=oldpeak,
            peak_ST_segment_slope=peak_ST_segment_slope,
            major_vessels=major_vessels,
            thal=thal,
            Gender=gen
        )
        pred_obj.save()
        
        datas={
            'age':pred_obj.age,
            'Chest_pain_type':pred_obj.Chest_pain_type,
            'resting_blood_pressure':pred_obj.resting_blood_pressure,
            'serum_cholestoral':pred_obj.serum_cholestoral,
            'fasting_blood_sugar':pred_obj.fasting_blood_sugar,
            'resting_electrocardiographic':pred_obj.resting_electrocardiographic,
            'max_heart_rate':pred_obj.max_heart_rate,
            'exercise_induced_angina':pred_obj.exercise_induced_angina,
            'oldpeak':pred_obj.oldpeak,
            'peak_ST_segment_slope':pred_obj.peak_ST_segment_slope,
            'major_vessels':pred_obj.major_vessels,
            'thal':pred_obj.thal,
            'Gender':pred_obj.Gender
        }
        # changing types of value
        #thal value
        thal=0
        if(datas["thal"]=="normal"):
            thal=0
        elif(datas["thal"]=="fixed defect"):
            thal=1
        else:
            thal=2

        #major vessels value
        major_vessels=0
        if(datas["major_vessels"]=="0"):
            major_vessels=0
        elif(datas["major_vessels"]=="1"):
            major_vessels=1
        elif(datas["major_vessels"]=="2"):
            major_vessels=2
        else:
            major_vessels=3

        # peak ST segment Slope
        peak_ST_segment_slope=0
        if(datas["peak_ST_segment_slope"]=="upsloping"):
            peak_ST_segment_slope=0
        elif(datas["peak_ST_segment_slope"]=="flat"):
            peak_ST_segment_slope=1
        else:
            peak_ST_segment_slope=2

        # exercise induced angina
        exercise_induced_angina=0
        if(datas["exercise_induced_angina"]=="No"):
            exercise_induced_angina=0
        else:
            exercise_induced_angina=1

        # restin electro card
        resting_electrocardiographic=0
        if(datas["resting_electrocardiographic"]=="Normal"):
            resting_electrocardiographic=0
        elif(datas["resting_electrocardiographic"]=="having ST-T"):
            resting_electrocardiographic=1
        else:
            resting_electrocardiographic=2

        #fating bood sugar
        fasting_blood_sugar=0
        if(datas["fasting_blood_sugar"]=="fbs < 120 mg/dl"):
            fasting_blood_sugar=0
        else:
            fasting_blood_sugar=1
        

        #chest pain type
        Chest_pain_type=0
        if(datas["Chest_pain_type"]=="typical angina"):
            Chest_pain_type=0
        elif(datas["Chest_pain_type"]=="typical angina"):
            Chest_pain_type=1
        elif(datas["Chest_pain_type"]=="non-anginal pain"):
            Chest_pain_type=2
        else:
            Chest_pain_type=3


        # gender check
        sex=0
        if(datas["Gender"]=="male"):
            sex=1
        else:
            sex=0
        
        #model prediction part
        input_data = (
            datas['age'],
            sex,Chest_pain_type,
            int(datas['resting_blood_pressure']),
            int(datas['serum_cholestoral']),
            fasting_blood_sugar,
            resting_electrocardiographic,
            datas['max_heart_rate'],
            exercise_induced_angina,
            datas['oldpeak'],
            peak_ST_segment_slope,
            major_vessels,
            thal
        )
        for i in input_data:
            print(type(i))
        # change the input data to a numpy array
        input_data_as_numpy_array= np.asarray(input_data)

            # reshape the numpy array as we are predicting for only on instance
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
        prediction = model.predict(input_data_reshaped)
        print(prediction)
        return render(request,'result.html',datas)
    else:
        return redirect('prdictformpage')

def edit_form(request): 
    obj = predict_form.objects.latest('added_on')
    datas={
            'age':obj.age,
            'Chest_pain_type':obj.Chest_pain_type,
            'resting_blood_pressure':(obj.resting_blood_pressure),
            'serum_cholestoral':obj.serum_cholestoral,
            'fasting_blood_sugar':obj.fasting_blood_sugar,
            'resting_electrocardiographic':obj.resting_electrocardiographic,
            'max_heart_rate':obj.max_heart_rate,
            'exercise_induced_angina':obj.exercise_induced_angina,
            'oldpeak':obj.oldpeak,
            'peak_ST_segment_slope':obj.peak_ST_segment_slope,
            'major_vessels':obj.major_vessels,
            'thal':obj.thal,
            'Gender':obj.Gender
        }
    return render(request,'edit_prediction_form.html',datas)

def save_form(request): 
    context={}
    data=predict_form()
    if request.method=="POST":
        age=int(request.POST["age"])
        Chest_pain_type=request.POST["cpt"]
        resting_blood_pressure=request.POST["rbp"]
        serum_cholestoral=request.POST["sc"]
        fasting_blood_sugar=(request.POST["fbs"])
        resting_electrocardiographic=(request.POST["re"])
        max_heart_rate=int(request.POST["mhr"])
        exercise_induced_angina=(request.POST["eia"])
        oldpeak=float(request.POST["op"])
        peak_ST_segment_slope=(request.POST["peakst"])
        major_vessels=int(request.POST["mv"])
        thal=(request.POST["thal"])
        gen=request.POST["gender"]

        current_user=request.user

        #updating the prediction table
        data.age = age
        data.Chest_pain_type = Chest_pain_type
        data.resting_blood_pressure=resting_blood_pressure
        data.serum_cholestoral=serum_cholestoral
        data.fasting_blood_sugar=fasting_blood_sugar
        data.resting_electrocardiographic=resting_electrocardiographic
        data.max_heart_rate=max_heart_rate
        data.exercise_induced_angina=exercise_induced_angina
        data.oldpeak=oldpeak
        data.peak_ST_segment_slope=peak_ST_segment_slope
        data.major_vessels=major_vessels
        data.thal=thal
        data.Gender=gen
        user_name=current_user.username
        #saving the data
        data.save()
        datas={
            'age':data.age,
            'Chest_pain_type':data.Chest_pain_type,
            'resting_blood_pressure':int(data.resting_blood_pressure),
            'serum_cholestoral':int(data.serum_cholestoral),
            'fasting_blood_sugar':data.fasting_blood_sugar,
            'resting_electrocardiographic':data.resting_electrocardiographic,
            'max_heart_rate':data.max_heart_rate,
            'exercise_induced_angina':data.exercise_induced_angina,
            'oldpeak':data.oldpeak,
            'peak_ST_segment_slope':data.peak_ST_segment_slope,
            'major_vessels':data.major_vessels,
            'thal':data.thal,
            'Gender':data.Gender
        }

        # changing types of value
        #thal value
        thal=0
        if(datas["thal"]=="normal"):
            thal=0
        elif(datas["thal"]=="fixed defect"):
            thal=1
        else:
            thal=2

        #major vessels value
        major_vessels=0
        if(datas["major_vessels"]=="0"):
            major_vessels=0
        elif(datas["major_vessels"]=="1"):
            major_vessels=1
        elif(datas["major_vessels"]=="2"):
            major_vessels=2
        else:
            major_vessels=3

        # peak ST segment Slope
        peak_ST_segment_slope=0
        if(datas["peak_ST_segment_slope"]=="upsloping"):
            peak_ST_segment_slope=0
        elif(datas["peak_ST_segment_slope"]=="flat"):
            peak_ST_segment_slope=1
        else:
            peak_ST_segment_slope=2

        # exercise induced angina
        exercise_induced_angina=0
        if(datas["exercise_induced_angina"]=="No"):
            exercise_induced_angina=0
        else:
            exercise_induced_angina=1

        # restin electro card
        resting_electrocardiographic=0
        if(datas["resting_electrocardiographic"]=="Normal"):
            resting_electrocardiographic=0
        elif(datas["resting_electrocardiographic"]=="having ST-T"):
            resting_electrocardiographic=1
        else:
            resting_electrocardiographic=2

        #fating bood sugar
        fasting_blood_sugar=0
        if(datas["fasting_blood_sugar"]=="fbs < 120 mg/dl"):
            fasting_blood_sugar=0
        else:
            fasting_blood_sugar=1
        

        #chest pain type
        Chest_pain_type=0
        if(datas["Chest_pain_type"]=="typical angina"):
            Chest_pain_type=0
        elif(datas["Chest_pain_type"]=="typical angina"):
            Chest_pain_type=1
        elif(datas["Chest_pain_type"]=="non-anginal pain"):
            Chest_pain_type=2
        else:
            Chest_pain_type=3


        # gender check
        sex=0
        if(datas["Gender"]=="male"):
            sex=1
        else:
            sex=0
        
        #model prediction part
        input_data = (
            datas['age'],
            sex,
            Chest_pain_type,
            datas['resting_blood_pressure'],
            datas['serum_cholestoral'],
            fasting_blood_sugar,
            resting_electrocardiographic,
            datas['max_heart_rate'],
            exercise_induced_angina,
            datas['oldpeak'],
            peak_ST_segment_slope,
            major_vessels,
            thal
        )
        # change the input data to a numpy array
        input_data_as_numpy_array= np.asarray(input_data)

        # reshape the numpy array as we are predicting for only on instance
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

        prediction = model.predict(input_data_reshaped)
        datas["prediction"]=prediction[0]
        print(prediction[0])
        return render(request,'result.html',datas)   
    else:
        return render(request,'result.html')
 

def locate(request):
    return render(request,'search.html')
        