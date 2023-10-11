mathText = ""

usedValues = []
targetChar = 9007199254740992
old = targetChar
operators = []
targetText = document.getElementById("currentMath")

function updateCurrentMath(args) {

        mathText = mathText + args
        targetText.innerHTML = mathText
    
    if(old != targetChar)
        old = old + args
    else
        old = "0" + args
}

function addOperator(args){
    if(!mathText.endsWith('÷') && !mathText.endsWith("x") && !mathText.endsWith("-") && !mathText.endsWith("+")){
        operators.push(args)
        if(mathText == ""){
            mathText = "0" + args
            targetText.innerHTML = mathText
        }
        else
        {
            mathText = mathText + args
            targetText.innerHTML = mathText
        }
        
        sendOld()
    }
    
}

function clearCurrentMath() {
    mathText = ""
    targetText.innerHTML = "0"
    usedValues.length = 0
    operators.length = 0
}

function calculateEvent(){
    
    calculation = 0
    
    if(!mathText.endsWith('÷') && !mathText.endsWith("x") && !mathText.endsWith("-") && !mathText.endsWith("+") && old !== NaN){
        sendOld()
        console.log("Used Values in order:")
        usedValues.forEach(
            function(oldValue){
                console.log(oldValue)
            }
        )

        console.log("Used Operators in order:")
        operators.forEach(
            function(usedOperator){
                console.log(usedOperator)
            }
        )


        // CALCULATION:
        usedValues.forEach(
            function(usedValue){
                tempValue = 0
                tempValue = usedValue
                operators.forEach(
                    function(operator){
                        // calculation will be: get each value from usedValues-list and use it's index to get the operator from operators-list
                        
                    }
                )
            })

        console.log(calculation.toString())
    }
    else
    {
        console.log("Last one is not a number!")
    }
    
}

function sendOld(){
    if(old != targetChar){
        usedValues.push(parseFloat(old))
        old = targetChar
    }
        
}