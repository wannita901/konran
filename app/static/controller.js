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

// createDiv(json_test)
document.addEventListener('DOMContentLoaded', (event) => {
    var text_content = document.getElementById("bullets").textContent;
    text_content = text_content.trim()
    console.log(text_content)   
    if (text_content === "EMPTY"){

    }
    else{
    var json_test = JSON.parse(text_content)
    console.log(json_test)
    createDiv(json_test)
    }
})
