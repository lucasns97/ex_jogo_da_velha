def get_heuristica(board, deep, player_maximizer):
  '''
  Função que retorna heurística do tabuleiro para o minimax
  '''

  # Se é folha / tabuleiro completo => retorna heurística
  done, winner = board.is_done()
  if done:

    if winner:
      # vencedor
      if winner == player_maximizer:
        return True, 2

      # derrotado
      else:
        return True, -2

    else:
      # empate
      return True, 0

  # Atingiu profundidade máxima na árvore
  if deep == 0:
    return True, -1

  return False, None

def max_val(board, deep, player_maximizer, alpha=-9999999, beta=9999999):
  '''
  Função que retorna o max_val do minimax c/ alpha/beta prunning
  '''

  done, heuristica = get_heuristica(board, deep, player_maximizer)
  if done:
    return heuristica

  val          = -9999999
  for player in board.players:
    if player == player_maximizer:
      player_piece = player.piece

  for pos in board.available_pos:

    new_board = board.copy_board()

    new_board.add_piece(player_piece, pos)

    val   = max(val, min_val(new_board, deep-1, player_maximizer, alpha, beta))
    alpha = max(alpha, val)

    if alpha >= beta:
      break
  
  return val

def min_val(board, deep, player_maximizer, alpha=-9999999, beta=9999999):
  '''
  Função que retorna o min_val do minimax c/ alpha/beta prunning
  '''

  done, heuristica = get_heuristica(board, deep, player_maximizer)
  if done:

    return heuristica

  val          = 9999999

  for player in board.players:
    if player != player_maximizer:
      player_piece = player.piece

  for pos in board.available_pos:

    new_board = board.copy_board()

    new_board.add_piece(player_piece, pos)

    val  = min(val, max_val(new_board, deep-1, player_maximizer, alpha, beta))
    beta = min(beta, val)

    if beta <= alpha:
      break
  
  return val