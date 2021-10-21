function wait(timeout) {
    return new Promise(resolve => {
        setTimeout(resolve, timeout);
    });
}


document.querySelectorAll(`a.-nal3 `)[0].click();

await wait(10000);

document.querySelector(`div.PZuss`).click();


await wait(2000);

var carica = setInterval(function () { document.querySelector('.PZuss').scrollIntoView(false); },
    900);


setTimeout(function () {
    clearInterval(carica);
}, 30000);


await wait(34000);



var igusernames = document.querySelectorAll('.FPmhX.notranslate._0imsa');

var myusernames = [];

var x = igusernames.length;

var count = 0; igusernames.forEach((singleusername) => { myusernames[count] = singleusername.textContent; count++ })

console.log(x)
const makeCSV = (data) => {
    const rows = [];
  
    for (let i = 0; i < data.length; i++) {
      rows.push(`${data[i]}`);
    }
  
    return rows.join('\n');
  };
  
  
  const csv = makeCSV(myusernames);


var link = window.document.createElement("a");
link.setAttribute("href", "data:text/csv;charset=utf-8,%EF%BB%BF" + encodeURI(csv));
link.setAttribute("download", "following.csv");
link.click(); 
