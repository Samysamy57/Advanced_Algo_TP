// Implement UserBST structure 
class UserBST{
  int user_id; 
  String []friends_list = new String[];
  String name;
  name = 'Certo'
  boolean left, right;
  Node UserBST(Node friends_list, int user_id) {
    if friends_list == NULL {
      UserBST = false;
    }  
    else {
      if user_id = friends_list(name){
        UserBST = true;
      }
      else {
        if user_id < friends_list(name) {
          UserBST = UserBST(user_id, friends_list(left))
        }
        else{
          UserBST = UserBST(user_id, friends_list(right))
        }
      }
    }
  }
// Function FIND
  static boolean find(user_id){
    if friends_list == NULL {
      System.out.print("User not found")
    }
    else{
      if name = friends_list(user_id){
        find = true
          if name < friends_list(user_id){
            find = find(name, friends_list(left))
          }
              else{
                find = find(name, friends_list(right))
              }
    } // END IF
  } // END IF
  } // END FIND
// FUNCTION
  
} // END STRUCTURE

