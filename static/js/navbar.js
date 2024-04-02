// $(document).ready(function(){
// 	// Activate tooltip
// 	$('[data-toggle="tooltip"]').tooltip();
	
// 	// Select/Deselect checkboxes
// 	var checkbox = $('table tbody input[type="checkbox"]');
// 	$("#selectAll").click(function(){
// 		if(this.checked){
// 			checkbox.each(function(){
// 				this.checked = true;                        
// 			});
// 		} else{
// 			checkbox.each(function(){
// 				this.checked = false;                        
// 			});
// 		} 
// 	});
// 	checkbox.click(function(){
// 		if(!this.checked){
// 			$("#selectAll").prop("checked", false);
// 		}
// 	});
// });
// // document.addEventListener('DOMContentLoaded', function() {
// //     document.getElementById('menu-bar').addEventListener('click', function() {
// //         document.getElementById('content-side-bar').classList.toggle('sidebar-hidden');
// //     });

    
// //     document.querySelector('.profile-menu').addEventListener('click', function() {
// //         if (confirm('Are you sure you want to log out?')) {
// //             window.location.href = '/register';
// //         }
// //     });
// // });


// // manage_user

// <!DOCTYPE html>
// <html lang="en">
// <head>
//     <meta charset="UTF-8">
//     <meta name="viewport" content="width=device-width, initial-scale=1.0">
//     <link href="https://cdn.jsdelivr.net/npm/remixicon@4.2.0/fonts/remixicon.css" rel="stylesheet"/>
//     {% comment %} <link rel="stylesheet" href="{% static 'css/manage_user.css' %}"> {% endcomment %}
//     <title>Welcome to the manage user Page</title>
// </head>
// <body>

//     <html lang="en">
// <head>
//     <meta charset="UTF-8">
//     <meta name="viewport" content="width=device-width, initial-scale=1.0">
//     <style>
//         body {
//             font-family: Arial, sans-serif;
//             margin: 0;
//             padding: 0;
//         }

//         .header {
//             background-color:black;
//             margin-top: 20px;
//             padding: 10px;
//             height: 30px;
//             width: 91.5em;
//             color: rgb(255, 254, 254);
//             display: flex;
//             align-items: center;
//             margin-left: 320px;
//             justify-content: space-around;
//             border-radius: 15px ;
//             border: 3px solid rgb(255, 255, 255);
//             background-color:  #061d3c;
//             box-shadow: 0 1px 10px rgba(10,0,0,0.3), 0 0 0px rgba(0,0,0,0.1) inset;
//             font-size: 10px;
//         }


//         .nav {
//             display: flex;
//             list-style: none;
//             padding: 0;
//             margin: 0;
//             gap: 15px;
//             background-color: #ddd;
//             border-bottom: 1px solid #ccc;
//             border-top: 1px solid #ccc;
//         }

//         .nav a {
//             display: block;
//             padding: 15px;
//             color: #333;
//             text-decoration: none;
//             transition: background-color 0.3s;
//         }

//         .nav a:hover {
//             background-color: #eee;
//         }

//         .main-content {
//             display: flex;
//             flex-wrap: wrap;
//             gap: 15px;
//             padding: 15px;
//             margin-left: 40px;
//             height:400px;
//             width:65%;
        
//         }

//         .card-container {
//             width: 100%;
//             border: 1px solid #ddd;
//             border-radius: 5px;
//             background-color: white;
//             box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
//             margin-left: 270px;
          
//         }

//         .card-header {
//             display: flex;
//             justify-content: space-between;
//             align-items: center;
//             padding: 15px;
//             background-color: #f5f5f5;
//             border-bottom: 1px solid #ddd;
//             border-radius: 5px 5px 0 0;
//             margin:0px;

//         }

//         .card-content {
//             display: flex;
//             flex-direction: column;
//             padding: 15px;
//             gap: 10px;

//         }

//         .card-row {
//             display: flex;
//             align-items: center;
//             justify-content: space-between;
            
//         }

//         .card-row span {
//             color: #777;
//         }

//         .card-actions {
//             display: flex;
//             gap: 10px;
//         }

//         .action-button {
//             padding: 1px 7px;
//             height: 30px;
//             border-radius: 3px;
//             border: 1px solid #333;
//             background-color: transparent;
//             color: #333;
//             display:flex;
//             align-items:center;
//             text-transform: lowercase;
//             cursor: pointer;
//             transition: background-color 0.3s;
//             margin-right: 10px; /* Add margin to create space between buttons */

//         }

//         .action-button:last-child {
//             margin-right: 0px; 
//         }

//         .action-button:hover {
//             background-color: #333;
//             color: white;

//         }

//      {% comment %} ?? {% endcomment %}

    

//     .table-container {
//         width: 100%;
//         border-collapse: collapse;
//         margin-left: 0px;
//         background-color:yellow;


//     }

//     .table-header {
//     background-color: #f5f5f5;
//     border-bottom: 1px solid #ddd;
//     margin-left: 0px;
//     margin-top: 10px;
//     width: 100%;
//     display: flex;
//     justify-content: space-between;
// }

// .table-header th {
//     padding: 15px 45px;
//     text-align: left;
//     color: #333;
//     font-weight: normal;
//     flex: 1; /* Distribute available space equally among table headers */
// }

//     .table-content {
//         border-bottom: 1px solid #ddd;
//         margin-top: 10px;
//         height:60px;
//         background-color:green;
//         display:flex;
//         align-items:center;
//         justify-content:space-between;
//         padding:5px 40px;

//     }

//     .table-content td {
//         margin-left:30px;
//         width:146px;
//         padding:0px 10px;
//         margin-right:0px;
//         display:flex;
//         align-items:center;
//         justify-content: space-between; 
        
//     }


//     .table-content tr {
//         display: flex; 
//         justify-content: space-between; 
//         margin-left:-43px;
//         align-items:center;
//         justify-content: space-between; 
//         display:flex;
        
//     }
    
//     .table-content td {
//         border-top: 1px solid #ddd;
//         text-align: left;
//     }
    
//     .table-content tr:nth-child(even) {
//         background-color: #f5f5f5;
        
//     }
    
//     .table-content tr:last-child td {
//         background-color: red;
//     }
//     .table-footer {
//         display: flex;
//         justify-content: space-between;
//         align-items: center;
//         padding: 15px;
//         width:910px;
//         background-color: #f5f5f5;
//         margin-left:90px;
//         margin-top:30%;
//     }

//     .table-footer span {
//         color: #777;
//     }

//     .table-footer button {
//         padding: 5px 10px;
//         border-radius: 3px;
//         border: 1px solid #333;
//         background-color: transparent;
//         color: #333;
//         text-decoration: none;
//         text-transform: uppercase;
//         cursor: pointer;
//         transition: background-color 0.3s;
//     }

//     .table-footer button:hover {
//         background-color: #333;
//         color: white;
//     }
//     </style>
//     <title>Staff Members Example</title>
// </head>
// <body>
//     <div class="header">
//         <h1>Manage Users</h1>
//     </div>
//     <div class="main-content">
//         <div class="card-container">
//             <div class="card-header">
//                 <span>
//                     <span> <i class="ri-table-fill">   </i>List Of Users</span>
//                 </span>
//                 <div class="card-actions">
//                     <a class="action-button">Add Users</a>
//                 </div>
//             </div>
//             <div class="table-container">
//                 <table class="table-header">
//                     <thead>
//                         <tr>
//                             <th>User ID</th>
//                             <th>First Name</th>
//                             <th>Last Name</th>
//                             <th>Email</th>
//                             <th>Actions</th>
//                         </tr>
//                     </thead>
//                 </table>
//                 <div class="table-content">
//                     <table>
//                         <tbody>
//                             <tr>
//                                 <td>JKVN </td>
//                                 <td>SSA</td>
//                                 <td>AAA</td>
//                                 <td>AEE</td>
//                                 <td><a class="action-button"> <i class="ri-eye-fill"></i>View</a>
//                                     <a class="action-button"> <i class="ri-pencil-fill"></i>Edit</a>
//                                     <a class="action-button"> <i class="ri-delete-bin-6-fill"></i>Delete</a></td>
//                             </tr>
//                         </tbody>
//                     </table>
//                 </div>
//                 <div class="table-footer">
//                     <span>Showing 1 to 5 of 30 entries</span>
//                     <div>
//                         <button class="action-button">EXIT</button>
//                     </div>
//                 </div>
//             </div>
//         </body>
   
//     <script src="{% static 'js/navbar.js' %}"></script>
// </body>
// </html>



