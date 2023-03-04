function jsonToNode(json) {
    node = document.createElement("div")
    for (let topic in json) {
        // for (topic_item in json[topic]){
        //     text += topic + ": " + topic_item
        // }
        console.log(json[topic])
        text = document.createElement("text")
        name_node = document.createTextNode(topic)
        text.appendChild(name_node)
        node.appendChild(text)
        break_node = document.createElement("br")
        node.appendChild(break_node)
        
        for (topic_item in json[topic]) {
            console.log(json[topic][topic_item])
            text_value = document.createElement("text")
            value_node = document.createTextNode("- " + json[topic][topic_item])
            text_value.appendChild(value_node)
            node.appendChild(text_value)
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

var json_test = {
    "Data Privacy": [
        "Twitch collects personal information from its users, such as name, email address, and IP address.", 
        "Twitch uses this data to provide its services, including streaming video, chat, and other features.",
        "Twitch may also use this data to personalize content, improve its services, and provide targeted advertising.",
        "Twitch may share personal information with third parties in certain circumstances, such as to comply with legal obligations, protect users\u2019 rights, or to prevent fraud or abuse."
    ]
}

function createDiv(json){

    // console.log(document.getElementById("containerthing"))   
    document.getElementById("containerthing").appendChild(jsonToNode(json))
}

createDiv(json_test)