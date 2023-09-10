import express from "express"; 

import { PythonShell } from 'python-shell'



const app = express();

// Declaring the static middleware

app.use(express.static("public"));

// Makes req.body works (This is known as the middleware)
app.use(express.json());

// Section that lists all the available price plan starts here
app.post("/api/ucsvsr_model", function (req, res) {
    const DepthUnderground = req.body.DepthUnderground;
    const Density = req.body.Density;
    const UCS = req.body.UCS;
    const options = {

        args: [DepthUnderground, Density, UCS]
    }

    // run python code
    PythonShell.run('python-code/ucsvsr_model.py', options).then(messages => {
        console.log(messages)
        res.json(
            {
                "predictions": messages
            }
        );
    });
});

app.post("/api/srf_model", function (req, res) {
    
    const Virgin_stress_ratio = req.body.Virgin_stress_ratio;

    const options = {

        args: [Virgin_stress_ratio]
    }

    // run python code
    PythonShell.run('python-code/srf_model.py', options).then(messages => {
        console.log(messages)
        res.json(
            {
                "predictions": messages
            }
        );
     });
});
app.post("/api/Jn_model", function (req, res) {

    const description = req.body.description;

    const options = {

        args: description
    }


    // run python code
    PythonShell.run('python-code/jn_model.py', options)
    
    .then(messages => {
        console.log(messages)
        res.json(
            {
                "predictions": messages
            }
        );
    });
});
app.post("/api/Jr_model", function (req, res) {

    const description = req.body.description;

    const options = {

        args: [description]
    }

    // run python code
    PythonShell.run('python-code/jr_model.py', options).then(messages => {
        console.log(messages)
        res.json(
            {
                "predictions": messages
            }
        );
    });
});

app.post("/api/Ja_model", function (req, res) {

    const description = req.body.description;

    const options = {

        args: [description]
    }

    // run python code
    PythonShell.run('python-code/ja_model.py', options).then(messages => {
        console.log(messages)
        res.json(
            {
                "predictions": messages
            }
        );
    });
});
app.post("/api/Jw_model", function (req, res) {
    
    const description = req.body.description;

    const options = {

        args: [description]
    }

    // run python code
    PythonShell.run('python-code/jw_model.py', options).then(messages => {
        console.log(messages)
        res.json(
            {
                "predictions": messages
            }
        );
    });
});
app.post("/api/rqd_model", function (req, res) {
    
    const DepthFrom = req.body.DepthFrom;
    const DepthTo= req.body.DepthTo;
    const TrueThickness = req.body.TrueThickness;
    const Hardness = req.body.Hardness;

    const options = {

        args: [DepthFrom, DepthTo, TrueThickness,Hardness]
    }

    // run python code
    PythonShell.run('python-code/rqd_model.py', options).then(messages => {
        console.log(messages)
        res.json(
            {
                "predictions": messages
            }
        );
    });
});

app.post("/api/q_model", function (req, res) {				
    const RQD = req.body.RQD;
    const Jn = req.body.Jn;
    const Jr = req.body.Jr;
    const Ja = req.body.Ja;
    const Jw = req.body.Jw;
    const SRF = req.body.SRF;

    const options = {

        args: [RQD, Jn, Jr, Ja, Jw, SRF]
    }

    // run python code
    PythonShell.run('python-code/q_model.py', options).then(messages => {
        console.log(messages)
        res.json(
            {
                "predictions": messages
            }
        );
     });
});
app.post("/api/rmr_model", function (req, res) {
    		
    const Q_Value = req.body.Q_Value;

    const options = {

        args: [Q_Value]
    }

    // run python code
    PythonShell.run('python-code/rmr_model.py', options).then(messages => {
        console.log(messages)
        res.json(
            {
                "predictions": messages
            }
        );
     });
});

app.post("/api/esr_model", function (req, res) {
    
    const ESR_Conditions = req.body.ESR_Conditions;

    const options = {

        args: [ESR_Conditions]
    }

    // run python code
    PythonShell.run('python-code/esr_model.py', options).then(messages => {
        console.log(messages)
        res.json(
            {
                "predictions": messages
            }
        );
    });
});
app.post("/api/mus_model", function (req, res) {
    
    const Q_Value = req.body.Q_Value;
    const ESR_VALUE = req.body.ESR_VALUE;

    const options = {

        args: [Q_Value, ESR_VALUE]
    }

    // run python code
    PythonShell.run('python-code/mus_model.py', options).then(messages => {
        console.log(messages)
        res.json(
            {
                "predictions": messages
            }
        );
    });
});

// Adding our port listener which is by defualt
let PORT = process.env.PORT || 3008;

app.listen(PORT, function () {
  console.log("Capstone Project API with SQL starting on port", PORT);
});