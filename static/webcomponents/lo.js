import {LitElement, html} from 'https://unpkg.com/@polymer/lit-element@latest/lit-element.js?module';
        
export class LoComponent extends LitElement {
  static get properties () {
    return {mood: String}
  }
  
  render() {
    const {mood} = this || "OK";
    console.log(this);
    return html `
    <style>
    .lo {
      text-align: left; 
      margin-bottom: 20px; 
      padding: 20px !important;
      background-color: #c7c6c6
    }

    .lo-heading {
      color: black !important;
      font-size: 1rem !important; 
    }

    .lo-question {
      color: black !important;
      text-align: center;
    }
    </style>
    <div class="lo">
      <p class="lo-heading">LO Question:</p> 
      <p class="lo-question"><i><slot></slot></i></p>
      <div style="width: 100%; text-align: right; font-size: 1.5rem; display: flex; flex-direction: row">
        <img src="/static/modules/PDF_file_icon.svg" style="border: none !important; margin: 0px 0px 0px 0px !important; margin-right: 10px; width:40px; height: 40px; box-shadow: none!important"> 
        <a style="margin-left: 10px !important;" href="https://www.dropbox.com/s/nb6tnys10djmwgb/Module%20Description.pdf?dl=0">Link to Module Description</a>
      </div>
    </div>
    `
  }
}