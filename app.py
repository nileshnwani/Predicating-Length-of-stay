from flask import Flask, render_template, request
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

data = pd.read_csv('./Healthcare_Investments_and_Hospital_Stay (1).csv')

def onehot_encode(df, column):
    df = df.copy()
    dummies = pd.get_dummies(df[column])
    df = pd.concat([df, dummies], axis=1)
    df = df.drop(column, axis=1)
    return df

def preprocess_inputs(df):
    df = df.copy()
    df = onehot_encode(df, column='Location')
    y = df['Hospital_Stay'].copy()
    X = df.drop('Hospital_Stay', axis=1).copy()
    scaler = StandardScaler()
    scaler.fit(X)
    X_scaled = pd.DataFrame(scaler.transform(X), columns=X.columns)
    return X_scaled, y, scaler

X, y, scaler = preprocess_inputs(data)

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=123)

model = RandomForestRegressor()
model.fit(X_train, y_train)

vector = pd.Series(['AUS', 'AUT', 'BEL', 'CAN', 'CZE', 'DNK', 'FIN', 'FRA', 'DEU', 'GRC', 'HUN', 'IRL',
                    'ITA', 'JPN', 'KOR', 'LUX', 'NLD', 'NZL', 'POL', 'PRT', 'SVK', 'ESP', 'TUR', 'GBR',
                    'USA', 'EST', 'ISR', 'RUS', 'SVN', 'ISL', 'LVA', 'LTU'])

@app.route('/', methods=['GET', 'POST'])
def home():
    global vector  # Declare 'vector' as a global variable
    
    if request.method == 'POST':
        location = request.form['location'].lower()  # Convert location to lowercase
        time = float(request.form['time'])
        mriunits = float(request.form['mriunits'])
        ctscanners = float(request.form['ctscanners'])
        hospital_beds = float(request.form['hospital_beds'])
        
        new_value = pd.Series([location])
        vector = pd.concat([vector, new_value])
        
        new_data = pd.DataFrame({
            'Location': vector.values[-1:],  # Use only the last value of 'vector'
            'Time': [time],
            'MRI_Units': [mriunits],
            'CT_Scanners': [ctscanners],
            'Hospital_Beds':[hospital_beds]
        })
        
        
        
        new_data_encoded = onehot_encode(new_data, column='Location')
        new_data_encoded = new_data_encoded.reindex(columns=X_train.columns, fill_value=0)  # Align columns with X_train
        
        new_data_scaled = pd.DataFrame(scaler.transform(new_data_encoded), columns=new_data_encoded.columns)
        
        prediction = model.predict(new_data_scaled)
        
        return render_template('index.html', prediction=prediction)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)