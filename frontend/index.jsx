class App extends React.Component {
  constructor (props) {
    super(props);
    this.state = {
      "showDashBord" : false,
      "URLs" : false,
    }
  }
  render () {
    return <div className="cont">
        <h1>click to toggle dashbord</h1>
        <button onClick={() => {
            this.setState({ showDashBord: !this.state.showDashBord });
            this.setState({
              URLs: [{ title: "this is a url" }, { title: "this is a url" }]
            });
          }}>
          get links from dashbord
        </button>
        <ul>
          {" "}
          scraped URLs :
          {this.state.showDashBord && this.state.URLs.map(scraped => (
              <li>{scraped.title}</li>
            ))}
        </ul>
      </div>;
    }

}

console.log('before render')
ReactDOM.render(<App />, document.getElementById("App"));


//  () => {
//             $.ajax({
//               url: "http://127.0.0.1:3030/allScraped",
//               type: "GET",
//               success: data => {
  //                 ReactDOM.render(<dashbordList list={data} />, document.getElementById("container"));
  //               },
  //               error: err => {
    //                 console.log(err.message);
    //               }
    //             });
    //           }
    
    // list={[{ title: "title" }, { title: "title" }]}