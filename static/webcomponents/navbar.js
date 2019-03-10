import {LitElement, html} from 'https://unpkg.com/@polymer/lit-element@latest/lit-element.js?module';
      

export class NavbarComponent extends LitElement {
  
  static get properties () {
    return {}
  }
  
  render() {
    
    return html `
    <script src="/static/jQuery/jquery-3.3.1.slim.min.js" ></script>
    <script src="/static/bootstrap/dist/js/bootstrap.bundle.min.js"></script>
    <link  href="/static/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet" >
    <style>
      .nav-link {
        font-family: 'Open Sans Condensed';
      }
    </style>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <a class="navbar-brand" href="#">
          <img src="/static/SalihAvatar.png" width="30" height="30" alt="">
          <span style="font-family: 'poppins'">mrsalih.com</span>
        </a>
      <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
        
        <ul class="navbar-nav mr-auto mt-2 mt-lg-0">
          <li class="nav-item active">
            <a class="nav-link" href="/">Home <span class="sr-only">(current)</span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Modules</a>
          </li>
          <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          Dropdown
        </a>
        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
          <a class="dropdown-item" href="#">Action</a>
          <a class="dropdown-item" href="#">Another action</a>
          <div class="dropdown-divider"></div>
          <a class="dropdown-item" href="#">Something else here</a>
        </div>
      </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Clubs</a>
          </li>
          <!--
          <li class="nav-item">
            <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
          </li>
          -->
        </ul>
        <!--
        <form class="form-inline my-2 my-lg-0">
          <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
          <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
        </form>
        ---->
      </div>
    </nav>
    `;
    
  }
}

customElements.define('my-navbar', NavbarComponent);