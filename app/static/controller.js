function jsonToNode(json) {
    node = document.createElement("div")
    node.style.paddingTop = "20px"
    for (let topic in json) {
        // for (topic_item in json[topic]){
        //     text += topic + ": " + topic_item
        // }
        text = document.createElement("text")
        name_node = document.createTextNode(topic)
        text.style.fontWeight = "bold"
        text.appendChild(name_node)
        node.appendChild(text)
        break_node = document.createElement("br")
        node.appendChild(break_node)
        
        for (topic_item in json[topic]) {
            console.log(json[topic][topic_item])
            bullet_node = document.createElement("li")
            value_node = document.createTextNode(json[topic][topic_item])
            bullet_node.appendChild(value_node)
            bullet_node.style.paddingLeft = "20px"
            node.appendChild(bullet_node)
            
            // text_value = document.createElement("text")
            // value_node = document.createTextNode("- " + json[topic][topic_item])
            // text_value.appendChild(value_node)
            // node.appendChild(text_value)
            
            break_node = document.createElement("br")
            node.appendChild(break_node)
        }

        // for (let j = 0; j < json["values"].length(); j++){
        //    text += "<text>    - " + json["values"][j] + "</text>" + "<br>"
        // } 
    }
    console.log(text)
    
    // text_node = document.createTextNode(text)
    // node.appendChild(text_node)
    return node
  }

var json_ = {
    "topic1": ["1","2","3","4"],
    "topic2": ["a","b","c","d"]
}





function createDiv(json){
    // console.log(document.getElementById("containerthing"))   
    document.getElementById("containerthing").appendChild(jsonToNode(json))
}

// chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {    
//     let url = tabs[0].url;
//     document.getElementById("url").value=url
// });

// createDiv(json_test)
document.addEventListener('DOMContentLoaded', (event) => {
    
    var text_content = document.getElementById("bullets").textContent;
    text_content = text_content.trim()
    // console.log(text_content)
    if (text_content === "EMPTY"){

    }
    else{
    var json_test = JSON.parse(text_content)
    console.log(json_test)
    createDiv(json_test)

    }
})

function submitForm() {
    $('#checkButton').click(function() {
        $.ajax({
            url: 'http://127.0.0.1:5000/process',
            type: 'POST',
            data: {
                url: document.getElementById("url").textContent
            },
            success: function(msg) {
                alert('Email Sent');
            }               
        });
    });


    // var http = new XMLHttpRequest();
    // http.open("POST", "http://127.0.0.1:5000/process", true);
    // http.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    // var params = ; // probably use document.getElementById(...).value
    // http.send(params);
    // http.onload = function() {
    //     alert(http.responseText);
    // }
}

function spinnerOn(){
    // console.log("hello hello")
    // document.getElementById("spinner").style.display = "block";
    // create div for spinner
    spinner_div = document.createElement("div")
    spinner_div.className = "spinner-grow text-secondary"
    spinner_div.role = "status"
    spinner_div.style.position = "absolute"
    spinner_div.style.top = "20%"
    spinner_div.style.left = "45%"
    spinner_div.style.width = "5rem"
    spinner_div.style.height = "5rem"

    // create spinner span
    spinner_span = document.createElement("span")
    spinner_span.className = "sr-only"

    spinner_div.appendChild(spinner_span)
    
    // add to the card
    document.getElementById("containerthing").appendChild(spinner_div)
}

