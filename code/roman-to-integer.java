// Source : https://leetcode.com/problems/roman-to-integer/
// Author : Anabel Cristina
// Date   : 2023-05-30

/****************************************************/

class RomanToInt {
    public int romanToInt(String s) {
        char[] ch = s.toCharArray();

        int numero = 0;

        if (ch.length == 1) {
            switch (ch[0]){
                case 'I':
                    return 1;
                
                case 'V':
                    return 5;
                
                case 'X':
                    return 10;

                case 'L':
                    return 50;

                case 'C':
                    return 100;

                case 'D':
                    return 500;

                case 'M':
                    return 1000;

            }
        }

        for (int i = 0; i < ch.length; i++)
        {
            if(i < ch.length-1 && i != 0){
                switch (ch[i]){
                    case 'I':
                            if (ch[i+1] != 'V' && ch [i+1] != 'X')
                                numero += 1;                   
                    break;
                    
                    case 'V':
                        numero += ch[i-1] == 'I' ? 4 : 5;
                    break;
                    
                    case 'X':
        
                        if (ch[i-1] == 'I'){
                                numero += 9;
                            break;
                        }
                        

                        if (ch[i+1] != 'L' && ch[i+1] != 'C')
                            numero += 10;

                    break;

                    case 'L':
                            numero += i-1<0 ? 50 : (ch[i-1] == 'X' ? 40 : 50);
                    break;

                    case 'C':
                        
                        if (ch[i-1] == 'X'){
                            numero += 90;
                            break;
                        }

                        if (ch[i+1] != 'D' && ch[i+1] != 'M')
                            numero += 100;

                    break;  

                    case 'D':
                        numero += ch[i-1] == 'C' ? 400 : 500;
                    break;

                    case 'M':
                        numero += ch[i-1] == 'C' ? 900 : 1000;
                    break;
                
                }
            }
            else if (i == 0){
                switch (ch[i]){
                    case 'I':
                            if (ch[i+1] != 'V' && ch [i+1] != 'X')
                                numero += 1;                   
                    break;

                    case 'V':
                        numero += 5;
                    break;
                    
                    case 'X':
                        if (ch[i+1] != 'L' && ch[i+1] != 'C')
                            numero += 10;
                    break;

                    case 'L':
                            numero += 50;
                    break;

                    case 'C':   
                        if (ch[i+1] != 'D' && ch[i+1] != 'M')
                            numero += 100;
                    break;  

                    case 'D':
                        numero += 500;
                    break;

                    case 'M':
                        numero += 1000;
                    break;

                }
            }
            else {
                switch (ch[i]){
                    case 'I':
                        numero += 1;
                    break;
                    
                    case 'V':
                        numero += ch[i-1] == 'I' ? 4 : 5;
                    break;
                    
                    case 'X':
                        numero += ch[i-1] == 'I' ? 9 : 10;
                    break;

                    case 'L':
                        numero += ch[i-1] == 'X' ? 40 : 50;
                    break;

                    case 'C':
                        numero += ch[i-1] == 'X' ? 90 : 100;
                    break;

                    case 'D':
                        numero += ch[i-1] == 'C' ? 400 : 500;
                    break;

                    case 'M':
                        numero += ch[i-1] == 'C' ? 900 : 1000;
                    break;

                }
            }
        }
        return numero;
    }
}