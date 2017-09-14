var DnaTranscriber = function() {};

DnaTranscriber.prototype.toRna = function(input) {
    var mapping = {
        G: "C",
        C: "G",
        T: "A",
        A: "U"
    }

    var arr = input.split("");

    var newArr = arr.map(function(char) {
        if (mapping.hasOwnProperty(char))
            return mapping[char];
        else
            throw new Error("Invalid input")
    })

    return newArr.join("");
};

module.exports = DnaTranscriber;