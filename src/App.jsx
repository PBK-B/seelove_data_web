import React, { useState, useEffect, useRef } from "react";
import { WordCloud } from "@ant-design/charts";

import "./App.css";
import originDataDef from "./data/data.json";

const { data: originData } = originDataDef;

// var newData = [];
// originData.map((item, index) => {
//   if (item.value > 50) {
//     newData.push({
//       name: item.name,
//       value: item.value,
//     });
//   }
//   return null;
// });

function App() {
  const [data, setData] = useState([]);
  const oldData = useRef([]);

  useEffect(() => {
    // console.log("数据：", originData.length, newData);

    let index = 0;
    const size = 3;
    const timeval = window.setInterval(function () {
      const items = [];
      for (let i = 0; items.length < size && index < originData.length; i++) {
        const item = originData[index];
        if (item?.value > 5) {
          items.push(item);
          // console.log("数据", item);
        }
        index++;
      }
      pushDatas(items);

      if (index >= originData.length) {
        window.clearInterval(timeval);
        console.log("结束");
      }
    }, 750);
  }, []);

  var config = {
    data: data,
    wordField: "name",
    weightField: "value",
    colorField: "name",
    height: 700,
    wordStyle: {
      fontFamily: "Verdana",
      fontSize: [15, 120],
      rotation: 0,
    },
    random: function random() {
      return 0.5;
    },
  };

  const pushDatas = (msgs) => {
    let newMsgs = [...oldData.current];
    newMsgs = newMsgs.concat(msgs);
    oldData.current = newMsgs;
    setData(newMsgs);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1 className="header-title">看看爱情真实的模样。</h1>
        <p className="header-title header-sub-title">
          See what love looks like.
        </p>
      </header>
      <div>
        <WordCloud {...config} />
      </div>
    </div>
  );
}

export default App;
