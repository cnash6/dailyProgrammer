// Becuase I really want some kid to do a funcitonal answer to this one day

function compoundAdd(myNum) {
    var temp = myNum.toString().split("").reduce((prev, curr) => { return prev + parseInt(curr) }, 0)
    return temp > 9? compoundAdd(temp) : temp;
}

console.log(compoundAdd(515));