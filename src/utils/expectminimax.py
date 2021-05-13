import numpy as np

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

def expect_val(old_board, new_board, deep, origem, player_maximizer, expect_dist, max_expect_dist):
  '''
  Função que calcula o valor experado do expectminimax
  '''

  val = 0

  if origem == 'max':

    # Atingiu maximo de profundidade em não jogar
    if expect_dist >= max_expect_dist:
      val += 1 * expect_min_val(new_board, deep, player_maximizer, expect_dist = 0, max_expect_dist = max_expect_dist)

    else:
      # 0.5 chance de não mudar o tabuleiro
      val += (0.5) * expect_min_val(old_board, deep, player_maximizer, expect_dist = expect_dist + 1, max_expect_dist = max_expect_dist)

      # 0.5 chance de mudar o tabuleiro
      val += (0.5) * expect_min_val(new_board, deep, player_maximizer, expect_dist = 0, max_expect_dist = max_expect_dist)

  else:

    # Atingiu maximo de profundidade em não jogar
    if expect_dist >= max_expect_dist:
      val += 1 * expect_max_val(new_board, deep, player_maximizer, expect_dist = 0, max_expect_dist = max_expect_dist)

    else:

      # 0.5 chance de não mudar o tabuleiro
      val += (0.5) * expect_max_val(old_board, deep, player_maximizer, expect_dist = expect_dist + 1, max_expect_dist = max_expect_dist)

      # 0.5 chance de mudar o tabuleiro
      val += (0.5) * expect_max_val(new_board, deep, player_maximizer, expect_dist = 0, max_expect_dist = max_expect_dist)

  return val


def expect_max_val(board, deep, player_maximizer, expect_dist, max_expect_dist):
  '''
  Função que retorna o max_val do expectminimax
  '''

  done, heuristica = get_heuristica(board, deep, player_maximizer)
  if done:
    return heuristica

  val = -9999999

  for player in board.players:
    if player == player_maximizer:
      player_piece = player.piece

  for pos in board.available_pos:

    new_board = board.copy_board()

    new_board.add_piece(player_piece, pos)

    val = max(val, expect_val(board, new_board, deep-1, 'max', player_maximizer, expect_dist, max_expect_dist))

  return val

def expect_min_val(board, deep, player_maximizer, expect_dist, max_expect_dist):
  '''
  Função que retorna o min_val do expectminimax
  '''

  done, heuristica = get_heuristica(board, deep, player_maximizer)
  if done:
    return heuristica

  val = 9999999

  for player in board.players:
    if player != player_maximizer:
      player_piece = player.piece

  for pos in board.available_pos:

    new_board = board.copy_board()

    new_board.add_piece(player_piece, pos)

    val = min(val, expect_val(board, new_board, deep-1, 'min', player_maximizer, expect_dist, max_expect_dist))

  return val