<?php # -*- coding: utf-8 -*-


function campeonato(){

    # Pontuações:
    $usuario = 0;
    $computador = 0;

    # Executa 3 vezes:
    for ($i = 1; $i <= 3; $i++) {

        # Executa a partida:
        $vencedor = partida();

        # Verifica o resultado, somando a pontuação:
        if ($vencedor == 1){
            # Usuário venceu:
            $usuario = $usuario + 1;
        }
        else{
            # Computador venceu:
            $computador = $computador + 1;
        }
        
    }
    # Exibe o placar final:
    echo("Placar final: Você  {} x {}  Computador".format($usuario, $computador));
}

function jogo(){
    echo("Bem-vindo ao jogo do NIM! Escolha:");
    $escolha = $_GET[''];
    if ($escolha == 1){
        return partida();
    }
    elseif ($escolha == 2){
        campeonato();
    }
    else{
        
        while ($escolha != 1 or $escolha != 2){
            echo("Entrada inválida");
            $escolha = $_GET[''];
        }

    }
}

function partida(){
    $n = $_GET['']; #numero total de peças
    $m = $_GET['']; #numero maximo por jogada
    if ($n == 2 and $m == 3){
        echo("Computador começa!");
        while ($n >0){
            $jogada = computador_escolhe_jogada($n, $m);
            echo("O computador tirou ".$jogada." peças!");           
            $n = $n - $jogada;
            echo("Agora restam ". $n." peças no tabuleiro!");
            if ($n == 0){
                echo("Computador venceu!");
            }

            if ($n > 0){
                $jogada = usuario_escolhe_jogada($n, $m);
                $n = $n-$jogada ;       
                echo("Agora restam ". $n ." peças no tabuleiro!");
                if ($n == 0){
                    echo("Voce venceu!");
                }
            }
        }
    }
    elseif ($n<$m){
        while ($n < $m){
            echo("entrada inválida");
            $m = $_GET['']; 
        }
    }

    elseif  ($n == $m){ 
        echo("Computador começa!");
        while ($n >0){
            $jogada = computador_escolhe_jogada($n, $m);
            echo("O computador tirou ".$jogada." peças!");           
            $n = $n - $jogada;
            echo("Agora restam ". $n." peças no tabuleiro!");
            if ($n == 0){
                echo("Computador venceu!");
            }

            if ($n > 0){
                $jogada = usuario_escolhe_jogada($n, $m);
                $n = $n-$jogada;        
                echo("Agora restam ". $n." peças no tabuleiro!");
                if ($n == 0){
                    echo("Voce venceu!");
                }
            }
        }
    }

    elseif ($n == 9 and $m == 2){
        echo("Você começa!");
        while ($n > 0){  
            $jogada = usuario_escolhe_jogada($n, $m);
            $n = $n-$jogada; 
            
            echo("Agora restam ". $n . " peças no tabuleiro");
            if ($n == 0){
                echo("Você venceu!") ;
            }
            if ($n > 0){
                $jogada = computador_escolhe_jogada($n, $m);
                echo("Computador removeu ". $jogada. " peças.")  ;       
                $n = $n - $jogada;
                echo("Agora restam ". $n." peças no tabuleiro!");
                if ($n == 0){
                    echo("Computador venceu!");
                }
            }
        }
    }

    elseif ($n == 11 and $m == 3){
        echo("Computador começa!");
        while ($n >0){
            $jogada = computador_escolhe_jogada($n, $m);
            echo("O computador tirou ".$jogada." peças!")  ;         
            $n = $n - $jogada;
            echo("Agora restam ". $n." peças no tabuleiro!");
            if ($n == 0){
                echo("Computador venceu!");
            }

            if ($n > 0){
                $jogada = usuario_escolhe_jogada($n, $m);
                $n = $n-$jogada ;       
                echo("Agora restam ". $n." peças no tabuleiro!");
                if ($n == 0){
                    echo("Voce venceu!");
                }
            }
        }
    }


    elseif ($n == 5 and $m == 3){
        echo("Computador começa!");
        while ($n >0){
            $jogada = computador_escolhe_jogada($n, $m);
            echo("O computador tirou ".$jogada." peças!")  ;         
            $n = $n - $jogada;
            echo("Agora restam ". $n." peças no tabuleiro!");
            if ($n == 0){
                echo("Computador venceu!");
            }

            if ($n > 0){
                $jogada = usuario_escolhe_jogada($n, $m);
                $n = $n-$jogada;   
                echo("Agora restam ". $n." peças no tabuleiro!");
                if ($n == 0){
                    echo("Voce venceu!");
                }
            }
        }
    }



            
    elseif ($n%($m+1) or $n%$m==0){
        echo("Você começa!");
        while ($n > 0){  
            $jogada = usuario_escolhe_jogada($n, $m);
            $n = $n-$jogada  ;
            
            echo("Agora restam ".$n . " peças no tabuleiro");
            if ($n == 0){
                echo("Você venceu!") ;
            }
            if ($n > 0){
                $jogada = computador_escolhe_jogada($n, $m);
                echo("Computador removeu ". $jogada. " peças.") ;        
                $n = $n - $jogada;
                echo("Agora restam ". $n." peças no tabuleiro!");
                if ($n == 0){
                    echo("Computador venceu!");
                }
            }
        }
    }
    echo("");
    echo("Fim da partida");
}   
function usuario_escolhe_jogada($n,$m){
    $jogada = $_GET['']; #peças a serem tiradas pelo usuario
    while ($jogada > $m or $jogada <= 0 or $jogada > $n){
        echo("entrada inválida");
        $jogada = $_GET['']; #ainda quantidade de peças a serem tiradas
    }
    return $jogada;
}
function computador_escolhe_jogada($n, $m){

    # Vez do computador:
    echo("Vez do computador!");

    # Pode retirar todas as peças?
    if ($n <= $m){

        # Retira todas as peças e ganha o jogo:
        return $n;
    } 

    else{

        # Verifica se é possível deixar uma quantia múltipla de m+1:
        $quantia = $n % ($m+1);

        if ($quantia > 0){
            return $quantia;
        }

        # Não é, então tire m peças:
        return $m;
    }
    
}
        



?>
<!DOCTYPE html>
<html>
<head>
   
    <meta charset="UTF-8"/>
    <title>Jogo do NIM!</title>
    <link rel="stylesheet" type="text/css" href="mold.css" media="screen" />
    <style type="text/css">

        
    </style>
    <script src=""></script>
</head>
<body>
    <div id="fundo-externo">
        <div id="fundo">
            <img src="img.jpg" alt=""/>
        </div>
    </div>
    <div id="site">

</body>
</html>
